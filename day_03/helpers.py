def mul(mul_string: str) -> int:
  numbers_to_mul = list(map(int,mul_string.replace('mul(','').replace(')','').split(',')))
  return numbers_to_mul[0] * numbers_to_mul[1]
