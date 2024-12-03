def check_level(list : list[int]) -> bool:

  is_desc = False
  if list[0] > list[1]:
      is_desc = True

  for i in range(len(list)-1):
    if list[i] < list[i+1] and is_desc:
      return False
    if list[i] > list[i+1] and not is_desc:
      return False
    if abs(list[i] - list[i+1]) > 3:
      return False
    if list[i] == list[i+1]:
      return False
  return True