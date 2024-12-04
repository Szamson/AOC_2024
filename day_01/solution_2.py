import src

list_meshed = src.task_input.split()

first_list = [int(list_meshed[x]) for x in range(len(list_meshed)) if x % 2 == 0]
second_list = [int(list_meshed[x]) for x in range(len(list_meshed)) if x % 2 == 1]

list_count_dict = {}

for i in range(len(first_list)):
  if(not list_count_dict.__contains__(first_list[i])):
    list_count_dict[first_list[i]] = 0

for i in range(len(second_list)):
  if(list_count_dict.__contains__(second_list[i])):
    list_count_dict[second_list[i]] += 1

total_count = 0

for (k,v) in list_count_dict.items():
  total_count += k * v

print(total_count)