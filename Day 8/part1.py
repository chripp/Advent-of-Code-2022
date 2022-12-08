import numpy as np

def calc_visible(grid):
    grid_vis = np.zeros_like(grid, dtype=bool)
    temp = np.full_like(grid[0], -1)
    for i in range(len(grid)):
        grid_vis[i] = temp < grid[i]
        temp[grid_vis[i]] = grid[i, grid_vis[i]]
    return grid_vis

with open('input.txt') as f:
    lines = f.readlines()
grid = np.array(list(map(lambda x: list(map(int, x.rstrip('\n'))), lines)))
grid_vis = np.zeros_like(grid, dtype=bool)
grid_vis |= calc_visible(grid)
grid_vis |= calc_visible(grid.T).T
grid_vis |= np.flip(calc_visible(np.flip(grid, 0)), 0)
grid_vis |= np.flip(calc_visible(np.flip(grid.T, 0)), 0).T
score = grid_vis.sum()
print(score)