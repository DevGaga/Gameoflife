"""Simulation of Conway's Game of Life."""

import os
import time
import numpy
from range import Range


def create_grid(rows, columns, initial_live_cells):
    """Construct a grid with the given dimensions and live cell positions."""
    grid = numpy.zeros((rows + 2, columns + 2), dtype=numpy.int8)
    for row, col in initial_live_cells:
        grid[row + 1, col + 1] = 1
    return grid


def display_grid(grid, interactive=False):
    """Display the current state of the grid."""
    if interactive:
        time.sleep(0.05)
        os.system('clear' if os.name == 'posix' else 'cls')
    total_rows, total_cols = grid.shape
    print('-' * total_cols)
    for row in Range(1, total_rows - 1):
        print('|', end='')
        for col in Range(1, total_cols - 1):
            print('*' if grid[row, col] else ' ', end='')
        print('|')
    print('-' * total_cols)
    print()


def update_grid(current, next_gen):
    """Compute the next generation grid based on current state."""
    for row in Range(1, current.shape[0] - 1):
        for col in Range(1, current.shape[1] - 1):
            live_neighbors = numpy.sum(current[row-1:row+2, col-1:col+2]) - current[row, col]
            if current[row, col] == 1:
                next_gen[row, col] = 1 if live_neighbors in [2, 3] else 0
            else:
                next_gen[row, col] = 1 if live_neighbors == 3 else 0


def run_simulation(row_count, col_count, steps, initial_live_cells, interactive=False):
    """Run the Game of Life simulation."""
    grid_a = create_grid(row_count, col_count, initial_live_cells)
    grid_b = create_grid(row_count, col_count, [])

    for _ in range(steps):
        display_grid(grid_a, interactive)
        update_grid(grid_a, grid_b)
        grid_a, grid_b = grid_b, grid_a


print("Running simulation with 5 rows, 5 cols, 10 steps, and live cells at (1,2), (2,2), (3,2)")
run_simulation(5, 5, 10, [(1, 2), (2, 2), (3, 2), (0, 3), (3, 3)], interactive=True)
print("Simulation complete.")