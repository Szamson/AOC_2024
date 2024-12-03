import src

list_meshed = src.task_input.split()

first_list = [int(list_meshed[x]) for x in range(len(list_meshed)) if x % 2 == 0]
second_list = [int(list_meshed[x]) for x in range(len(list_meshed)) if x % 2 == 1]

first_list.sort()
second_list.sort()

count = 0
for i in range(len(first_list)) :
  count += abs(first_list[i] - second_list[i])

print(count)