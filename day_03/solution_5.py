import src, helpers
import re

regex = re.compile(r"mul\(\d{1,3},\d{1,3}\)")

operations_to_process = regex.findall(src.task_input)

operations_sum = 0
for operation in operations_to_process:
  operations_sum += helpers.mul(operation)

print(operations_sum)
