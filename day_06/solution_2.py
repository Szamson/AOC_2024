import src, helpers

matrix = src.task_input.split("\n")

orientation = [(-1, 0), (0, 1), (1, 0), (0, -1)]
guard_i, guard_j = -1, -1
guard_orientation_index = 0
path = set()
path_with_direction = set()
is_on_floor = True

for i in range(len(matrix)):
  for j in range(len(matrix[i])):
    if '^' == matrix[i][j]:
      guard_i, guard_j = i, j

def will_get_looped(guard_i, guard_j, direction_index):
  obs_i, obs_j = guard_i + orientation[direction_index][0], guard_j + orientation[direction_index][1]

  visited = {}
  helpers.add_element_to_dict(visited, (guard_i, guard_j), direction_index)

  while True:
    delta_i, delta_j = orientation[direction_index]
    next_gi, next_gj = guard_i + delta_i, guard_j + delta_j 
    
    if not (0 <= next_gi < len(matrix)) or not (0 <= next_gj < len(matrix[1])):
      return False

    if matrix[next_gi][next_gj] == '#' or (next_gi == obs_i and next_gj == obs_j):
      direction_index = (direction_index + 1) % 4
      continue

    if (next_gi, next_gj)  in visited and direction_index in visited[(next_gi, next_gj)]:
      return True

    guard_i, guard_j = next_gi, next_gj
    helpers.add_element_to_dict(visited, (guard_i, guard_j), direction_index)

loops = 0
while True:
  delta_i, delta_j = orientation[guard_orientation_index]
  next_gi, next_gj = guard_i + delta_i, guard_j + delta_j 
  
  if not (0 <= next_gi < len(matrix)) or not (0 <= next_gj < len(matrix[1])):
    break

  if matrix[next_gi][next_gj] == '#':
    guard_orientation_index = (guard_orientation_index + 1) % 4
    continue

  if (next_gi, next_gj) not in path and will_get_looped(guard_i, guard_j, guard_orientation_index):
    loops += 1

  guard_i, guard_j = next_gi, next_gj
  path.add((guard_i, guard_j))

print(loops)
