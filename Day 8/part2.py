import numpy as np

def calc_visible(grid):
    grid_vis = np.zeros_like(grid)
    for i in range(1, len(grid)):
        comp = np.ones_like(grid[i], dtype=bool)
        for r in range(i-1, -1, -1):
            grid_vis[i, comp] += 1
            comp[comp] &= grid[i, comp] > grid[r, comp]
            if not comp.any():
                break
    return grid_vis

with open('input.txt') as f:
    lines = f.readlines()
grid = np.array(list(map(lambda x: list(map(int, x.rstrip('\n'))), lines)))
grid_vis = calc_visible(grid) * calc_visible(grid.T).T * np.flip(calc_visible(np.flip(grid, 0)), 0) * np.flip(calc_visible(np.flip(grid.T, 0)), 0).T
print(grid_vis.max())