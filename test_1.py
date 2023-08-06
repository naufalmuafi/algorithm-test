import random
import time

def generate_value(V_old):
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
  V, total = 0, 0
  
  while True:
    V = generate_value(V)
    A.append(V)    
    print(f"Water Volume = {V} m^3/s\n")
    
    time.sleep(1)

if __name__ = "__main":
  main()