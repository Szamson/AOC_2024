import src, helpers

matrix = src.task_input.split("\n")

orientation = ['^','>','v','<']
current_guard_position = ()
current_guard_orientation_index = 0
path = {}
is_on_floor = True

for i in range(len(matrix)):
  for j in range(len(matrix[i])):
    if '^' == matrix[i][j]:
      current_guard_position = (i,j)

while(is_on_floor):

  if orientation[current_guard_orientation_index % 4] == '^':
    if helpers.check_obstacle(current_guard_position, orientation[current_guard_orientation_index % 4], matrix):
      current_guard_orientation_index += 1
      continue
    helpers.add_element_to_dict(path, current_guard_position)
    current_guard_position = (current_guard_position[0]- 1, current_guard_position[1])

  if orientation[current_guard_orientation_index % 4] == '>':
    if helpers.check_obstacle(current_guard_position, orientation[current_guard_orientation_index % 4], matrix):
      current_guard_orientation_index += 1
      continue
    helpers.add_element_to_dict(path, current_guard_position)
    current_guard_position = (current_guard_position[0], current_guard_position[1] + 1)

  if orientation[current_guard_orientation_index % 4] == 'v':
    if helpers.check_obstacle(current_guard_position, orientation[current_guard_orientation_index % 4], matrix):
      current_guard_orientation_index += 1
      continue
    helpers.add_element_to_dict(path, current_guard_position)
    current_guard_position = (current_guard_position[0] + 1, current_guard_position[1])

  if orientation[current_guard_orientation_index % 4] == '<':
    if helpers.check_obstacle(current_guard_position, orientation[current_guard_orientation_index % 4], matrix):
      current_guard_orientation_index += 1
      continue
    helpers.add_element_to_dict(path, current_guard_position)
    current_guard_position = (current_guard_position[0], current_guard_position[1] - 1)

  if (current_guard_position[0] >= len(matrix) - 1 and orientation[current_guard_orientation_index % 4] == 'v') or (current_guard_position[0] <= 0 and orientation[current_guard_orientation_index % 4] == '^') or (current_guard_position[1] >= len(matrix[1]) - 1 and orientation[current_guard_orientation_index % 4] == '>') or (current_guard_position[1] <= 0 and orientation[current_guard_orientation_index % 4] == '<'):
    helpers.add_element_to_dict(path, current_guard_position)
    is_on_floor = False

print(len(path))