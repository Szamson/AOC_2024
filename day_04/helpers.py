import re

regex = re.compile(r"XMAS")

def check_string_for_XMAS(input : str) -> int:
  xmas_count = 0
  xmas_count = len(regex.findall(input))

  reversed = input[::-1]
  xmas_count += len(regex.findall(reversed))

  return xmas_count