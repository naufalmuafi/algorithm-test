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
    elif V_new > 500:
      V_new = 500 - random.randint(1, 10)

    return V_new, cond

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
    V, condition = generate_value(V, condition)
    print(f"Water Volume = {V} m^3/s")
    
    total += V
    A.append(V)
    n = len(A)
    
    M = total/n
    print(f"Total = {total}, n = {n}")
    print(f"The average water volume at second {count} is {M:.3f} m^3/s\n")
    
    count += 1
    time.sleep(1)

main()