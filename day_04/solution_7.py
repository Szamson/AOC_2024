import src, helpers

matrix = src.task_input.split("\n")
# print(matrix)
transposed = [''.join(list(col)) for col in zip(*matrix)]
# print(transposed)

diagonals = {}
reversed_diagonals = {}

for i in range(len(matrix)):
  for j in range(len(matrix[i])):

    diag_index = i - j  
    reversed_diag_index = j + i

    if diag_index not in diagonals:
      diagonals[diag_index] = []
    if reversed_diag_index not in reversed_diagonals:
      reversed_diagonals[reversed_diag_index] = []

    diagonals[diag_index].append(matrix[i][j])
    reversed_diagonals[reversed_diag_index].append(matrix[i][j])

result = [''.join(diagonals[key]) for key in sorted(diagonals.keys())]
result_reversed = [''.join(reversed_diagonals[key]) for key in sorted(reversed_diagonals.keys())]
# print(result)
# print(result_reversed)

total_strings = matrix + transposed + result + result_reversed

total_xmas_count = 0
for item in total_strings:
  total_xmas_count += helpers.check_string_for_XMAS(item)

print(total_xmas_count)