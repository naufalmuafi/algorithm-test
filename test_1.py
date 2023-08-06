import random
import time

def generate_value(V_old, cond):
  if cond == 1:
    V_new = random.randint(1, 10)
    cond = 0
  
  V_new = random.randint(1, 1000)
  
  # timeout 0.1 second to the program
  time0 = time.time()
  
  while abs(V_old - V_new) > 10:
    V_new = random.randint(1, 1000)
    
    if(time.time() - time0 == 0.1):
      V_new = V_old + 10
    
  return V_new

def main():
  instruction = """
  
  ==============================================
  Welcome to Calculate Mean Program
  to stop the program, please enter Ctrl+C
  
  Naufal Mu'afi - nmuafi1@gmail.com
  ==============================================
  
  """
  print(instruction)
  time.sleep(5)
  
  A = []
  V, total, count, condition = 0, 0, 1, 1
  
  while True:
    V = generate_value(V, condition)
    print(f"Water Volume = {V} m^3/s")
    
    total += V
    A.append(V)
    length = len(A)
    
    M = total/length    
    print(f"The average water volume at second {count} is {M:.3f} m^3/s\n")
    
    count += 1
    time.sleep(1)

main()