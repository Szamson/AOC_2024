import src
from classes import PairOfAntennas 

def add_antenna(a_i, a_j, temp_cache : dict, roof):
  current_antenna = roof[a_i][a_j]
  temp_cache[(a_i, a_j)] = current_antenna

def calculate_dif(signal, roof_cache : dict, pair_of_antennas_set : set):
  values = [x for x in roof_cache.keys() if roof_cache[x] == signal]
  for i in range(len(values)):
    for j in range(len(values)):
      if i == j : 
        continue      
      pair_of_antennas_set.add(PairOfAntennas(values[i],values[j], signal))
  
roof = [list(x) for x in src.task_input.split("\n")]

PairOfAntennas.max_m = len(roof)
PairOfAntennas.max_n = len(roof[1])

roof_cache_dict = {}
pair_of_antennas_set = set()

for i in range(len(roof)):
  for j in range(len(roof[i])):
    if roof[i][j] != ".":
      add_antenna(i, j, roof_cache_dict, roof)

unique_signals = set(roof_cache_dict.values())

for signal in unique_signals:
  calculate_dif(signal, roof_cache_dict, pair_of_antennas_set)

unique_tuples = set()

for sublist in [x.potential_anti_antennas for x in pair_of_antennas_set]:
    unique_tuples.update(sublist)

anti_count = 0
for point in unique_tuples:
  if roof[point[0]][point[1]] == ".":
    roof[point[0]][point[1]] = "#"
    anti_count += 1
  elif roof[point[0]][point[1]] == "#": 
    continue
  else:
    anti_count += 1

for a in roof:
  print(''.join(a))

print(anti_count)
