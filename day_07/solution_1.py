import src

def add_or_mul(sol, list : list[int]):
  # print(list)
  m = len(list) - 1
  format_str = f'0{m}b'
  for i in range(0, int('1'*m, 2) + 1):
    operation_str = format(i, format_str)
    print(operation_str)
    a = execute_operations(operation_str, list)
    print(f"{a}|{sol}")
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
  return count

a = src.test_input.split("\n")
all_sum = 0
for line in a:
  solution, numbers = line.split(":")
  if add_or_mul(int(solution), list(map(int, numbers.split()))):
    print(int(solution))
    all_sum += int(solution)

print(f"SOLUTION: {all_sum}")

# add_or_mul(292, [11, 6, 16, 20])