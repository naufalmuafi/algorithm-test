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

  # create a treshold 0 <= V <= 500
  if V_new < 0:
    V_new = 0 + random.randint(1, 10)
  elif V_new > 500:
    V_new = 500 - random.randint(1, 10)

  return V_new
    

def main():
  instruction = """
  
  ===============================================
         Welcome to Calculate Mean Program
      to stop the program please enter Ctrl+C
  
         Naufal Mu'afi - nmuafi1@gmail.com
  ===============================================
  
  """
  print(instruction)
  time.sleep(5)
  
  A = []
  V, total, count = 0, 0, 1
  
  while True:
    V = generate_value(V)
    print(f"Water Volume = {V} m^3/s")
    
    # sum of all water volume data
    total += V
    A.append(V)
    
    # calculate the length of array A
    n = len(A)
    
    # calculate the average of water volume per second
    M = total/n
    
    print(f"Total = {total}, n = {n}")
    print(f"The average water volume at second {count} is {M:.3f} m^3/s\n")
    
    # count is timer and sleep() is to delay the program
    count += 1
    time.sleep(1)

main()