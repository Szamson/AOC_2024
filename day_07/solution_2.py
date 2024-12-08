import numpy as np
import src

def add_or_mul(sol, list : list[int]):
  # print(list)
  m = len(list) - 1
  for i in range(0, int('2'*m, 3) + 1):
    operation_str = np.base_repr(i, base= 3)
    operation_str = '0' * (len('2'*m) - len(operation_str)) + operation_str
    # print(operation_str)
    a = execute_operations(operation_str, list)
    # print(f"{a}|{sol}")
    if a == sol:
      return True
  return False
    
def execute_operations(operation_str, list):
  count = list[0]

  for x in range(1,len(operation_str)+1):
    if operation_str[x - 1] == '0':
      count += list[x]
    if operation_str[x - 1] == '1':
      count *= list[x]
    if operation_str[x - 1] == '2':
      count = int(str(count) + str(list[x]))
  return count

a = src.task_input.split("\n")
all_sum = 0
for line in a:
  solution, numbers = line.split(":")
  if add_or_mul(int(solution), list(map(int, numbers.split()))):
    print(int(solution))
    all_sum += int(solution)

print(f"SOLUTION: {all_sum}")