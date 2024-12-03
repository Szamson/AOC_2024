import src
import helpers

list_meshed = src.task_input.split("\n")
src_matrix = [list(map(int, x.split())) for x in list_meshed]

safe_level_count = 0

for item in src_matrix:
  if(helpers.check_level(item)):
    safe_level_count += 1

print(safe_level_count)