import src
from collections import deque

mountain = [list(map(int,list(x))) for x in src.test_input.split("\n")]
trial_starts = set()

for i in range(len(mountain)):
  for j in range(len(mountain[i])):
    if mountain[i][j] == 0:
      trial_starts.add((i,j))

def dfs_iterative(grid, start_x, start_y):
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = set()
    path = []
    stack = [(start_x, start_y)]
    trail_score = 0
    trial_rating = 0
    while stack:
        x, y = stack.pop()
        if (x, y) in visited:
            continue
        
        visited.add((x, y))
        path.append((x, y))
        
        if grid[x][y] == 9:
           trail_score += 1

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited and grid[x][y] + 1 == grid[nx][ny]:
                trial_rating += 1
                stack.append((nx, ny))
    # print(path)
    return trial_rating

trial_count_score = 0
for start in trial_starts:
   visited = set()
   print(bfs_on_grid(mountain, start))


# print(trial_count_score)