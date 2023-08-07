import random
import time

def generate_value(V_old, cond):
  if cond == 1:
    V_new = random.randint(1, 10)
    cond = 0
    
    return V_new, cond
  else:
    if random.random() <= 0.7:      
      V_new = V_old + random.randint(1, 10)
    else:
      V_new = V_old - random.randint(1, 10)
    
    if V_new < 0:
      V_new = 0 + random.randint(1, 10)
    elif V_new > 1000:
      V_new = 1000 - random.randint(1, 10)

    return V_new, cond

def insertion_sort(data, value):
  for i, v in enumerate(data):
    if value <= v:
      sorted_data = data[:i] + [value] + data[i:]
      return sorted_data
  
  sorted_data = data + [value]
  return sorted_data

def print_data(data):
  n = len(data)
  mid = n // 2
  
  if n <= 20:
    print(f"A = {data} len = {n}")
  else:
    if n % 2 == 1:
      print(f"A = [..., {data[mid-1]}, {data[mid]}, {data[mid+1]}, ...] len = {n}")
    else:
      print(f"A = [..., {data[mid-2]}, {data[mid-1]}, {data[mid]}, {data[mid+1]}, ...] len = {n}")

def median(data):
  length = len(data)  
  middle = length // 2
  
  if length % 2 == 1:
    Median = data[middle]
  else:
    Median = (data[middle] + data[middle - 1]) / 2.0
  
  return Median

def main():
  instruction = """
  
  ===============================================
        Welcome to Calculate Median Program
      to stop the program please enter Ctrl+C
  
         Naufal Mu'afi - nmuafi1@gmail.com
  ===============================================
  
  """
  print(instruction)
  time.sleep(5)

  A = [0]
  V, count, condition = 0, 1, 1

  while True:
    V, condition = generate_value(V, condition)    
    print(f"Water Volume = {V} m^3/s")        
    
    A = insertion_sort(A, V)            
    M = median(A)    
    
    print_data(A)
    print(f"The median of water volume at second {count} is {M:.2f} m^3/s\n")

    count += 1
    time.sleep(1)


main()