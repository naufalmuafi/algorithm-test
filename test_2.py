# import module that we use
import random
import time

# this function is to generate random value
def generate_value(V_old):
  # create a increase value 70%, and decrease value 30%
  if random.random() <= 0.7:
    V_new = V_old + random.randint(1, 10)
  else:
    V_new = V_old - random.randint(1, 10)

  # create a treshold 0 <= V <= 1000
  if V_new < 0:
    V_new = 0 + random.randint(1, 10)
  elif V_new > 1000:
    V_new = 1000 - random.randint(1, 10)

  return V_new

# this function is to sort the array
def insertion_sort(data, value):
  for i, v in enumerate(data):
    if value <= v:
      sorted_data = data[:i] + [value] + data[i:]
      return sorted_data
  
  sorted_data = data + [value]
  return sorted_data

# this function is just to print the array
def print_data(data):
  n = len(data)
  mid = n // 2
  
  # if n <= 20, so it will print all the data
  if n <= 20:
    print(f"A = {data} len = {n}")
  else: # besides that, the array that printed is just the middle index.
    if n % 2 == 1:
      print(f"A = [..., {data[mid-1]}, {data[mid]}, {data[mid+1]}, ...] len = {n}")
    else:
      print(f"A = [..., {data[mid-2]}, {data[mid-1]}, {data[mid]}, {data[mid+1]}, ...] len = {n}")

# calculate the median
def median(data):
  length = len(data)  
  middle = length // 2 # this variable is to simplify
  
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
  V, count = 0, 1

  while True:
    V = generate_value(V)    
    print(f"Water Volume = {V} m^3/s")        
    
    A = insertion_sort(A, V)            
    M = median(A)
    
    print_data(A)
    print(f"The median of water volume at second {count} is {M:.2f} m^3/s\n")

    # count is timer and sleep() is to delay the program
    count += 1
    time.sleep(1)


main()