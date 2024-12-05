import re

regex = re.compile(r"XMAS")
regex_mas = re.compile(r"MAS")

def check_string_for_XMAS(input : str) -> int:
  xmas_count = 0
  xmas_count = len(regex.findall(input))

  reversed = input[::-1]
  xmas_count += len(regex.findall(reversed))

  return xmas_count

def check_for_x_max(x : int, y : int, matrix : list[str]) -> int:
  dia_1 = matrix[x-1][y-1] + matrix[x][y] + matrix[x+1][y+1]
  dia_2 = matrix[x-1][y+1] + matrix[x][y] + matrix[x+1][y-1]
  dia_3 = matrix[x+1][y-1]  + matrix[x][y] + matrix[x-1][y+1]
  dia_4 = matrix[x+1][y+1] + matrix[x][y] + matrix[x-1][y-1]

  return 1 if [bool(regex_mas.search(dia_1)), bool(regex_mas.search(dia_2)), bool(regex_mas.search(dia_3)), bool(regex_mas.search(dia_4))].count(True) > 1  else 0 