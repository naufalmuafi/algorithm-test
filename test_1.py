import random
import time

def generate_value(V_old, condition):
  if condition == 1:
    V_new = random.randint(1, 10)
    condition = 0
  
  V_new = random.randint(1)
  
  # timeout 0.5 second to the program
  time0 = time.time()
  
  while abs(V_old - V_new) > 10:
    V_new = random.randint(1)
    
    if(time.time() - time0 == 0.5):
      V_new = V_old + 10
    
  return V_new

def main():
  A = []
  V, total, count, condition = 0, 0, 1, 1
  
  while True:
    V = generate_value(V, condition)
    print(f"Water Volume = {V} m^3/s\n")
    
    total += V
    A.append(V)
    length = len(A)
    
    M = total/length    
    print(f"The average water volume at second {count} is {M} m^3/s")
    
    count += 1
    time.sleep(1)

if __name__ = "__main":
  main()