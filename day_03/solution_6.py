import src, helpers
import re

regex = re.compile(r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)")
do_str = 'do()'
dont_str = "don't()"

operations_to_process = regex.findall(src.task_input)

operations_sum = 0
add_mul = True
for operation in operations_to_process:
  if operation == do_str:
    add_mul = True
    continue
  if operation == dont_str:
    add_mul = False
    continue

  if(add_mul):
    operations_sum += helpers.mul(operation)

print(operations_sum)
