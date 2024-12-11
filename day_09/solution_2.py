import src
import time
from sortedcontainers import SortedDict

input = src.task_input

memory = []
free_space_dict = SortedDict()  
file_space_dict = {}
file_positions = {}  
memory_index = 0
file_id = 0

start_time = time.time()

for i in range(len(input)):
    file_length = int(input[i])
    if i % 2 == 0:  
        memory.extend([str(file_id)] * file_length)
        file_space_dict[file_id] = file_length
        file_positions[file_id] = memory_index 
        memory_index += file_length
        file_id += 1
    else:  
        free_space_dict[memory_index] = file_length
        memory_index += file_length
        memory.extend(['.'] * file_length)

print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()

for file_id in reversed(range(file_id)):
    file_size = file_space_dict[file_id]
    file_start = file_positions[file_id] 

    for free_start, free_size in free_space_dict.items():
        if free_start + free_size <= file_start and free_size >= file_size:
            memory[free_start:free_start + file_size] = memory[file_start:file_start + file_size]
            memory[file_start:file_start + file_size] = ['.'] * file_size
            
            free_space_dict.pop(free_start)
            if free_size > file_size:
                free_space_dict[free_start + file_size] = free_size - file_size
            
            free_space_dict[file_start] = file_size
            
            file_positions[file_id] = free_start
            
            break 

print("--- %s seconds ---" % (time.time() - start_time))
print("Sorting done")
start_time = time.time()

check_sum = sum(i * int(memory[i]) for i in range(len(memory)) if memory[i] != '.')

print("--- %s seconds ---" % (time.time() - start_time))
print(check_sum)
