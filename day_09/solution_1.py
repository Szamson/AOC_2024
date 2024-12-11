import src
import time

input = src.task_input

start_time = time.time()

# Optimize memory population
memory = []
file_sum_space = 0
file_id = 0

for i in range(len(input)):
    file_length = int(input[i])
    if i % 2 == 0:
        memory.extend([str(file_id)] * file_length)
        file_sum_space += file_length
        file_id += 1
    else:
        memory.extend(['.'] * file_length)

print("--- %s seconds ---" % (time.time() - start_time))
print(f"File space: {file_sum_space}")
start_time = time.time()

# Optimize the sorting loop with two-pointer technique
left = 0
right = len(memory) - 1

while left < right:
    while left < len(memory) and memory[left] != '.':
        left += 1
    while right > left and memory[right] == '.':
        right -= 1
    if left < right:
        memory[left], memory[right] = memory[right], memory[left]
        left += 1
        right -= 1

print("--- %s seconds ---" % (time.time() - start_time))
print("Sorting done")
start_time = time.time()

# Optimize checksum calculation
check_sum = sum(i * int(memory[i]) for i in range(file_sum_space) if memory[i] != '.')

print("--- %s seconds ---" % (time.time() - start_time))
print(check_sum)
