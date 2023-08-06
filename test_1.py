import random
import time

def generate_value(V):
  V_new = random.randint(1)
  
  while abs(V - V_new) > 10:
    V_new = random.randint(1)
    
  return V_new

def main():
  
  
  while True:
    
    
    time.sleep(1)

if __name__ = "__main":
  main()