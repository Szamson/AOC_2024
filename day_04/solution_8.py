import src, helpers

matrix = src.task_input.split("\n")

x_mas_count = 0
for i in range(1, len(matrix)-1):
  for j in range(1, len(matrix[i])-1):
    x_mas_count += helpers.check_for_x_max(i, j, matrix)

print(x_mas_count)
