import pdb  # Python debugger
import numpy as np
from termcolor import colored

with open('11-1-input.txt', 'r') as f:
    stri = list( f.read() )

## Number of columns and rows was already revealed in puzzle text
n_rows = 10
n_cols = 10

## parsing:
grid = np.zeros((n_rows, n_cols))
for i in range(n_rows):
    for j in range(n_cols):
        grid[i,j] = float(stri.pop(0))
    assert(stri.pop(0) == '\n')
assert(stri == [])



def adjacent_indices(i,j):
    naive_adjacent_indices = [
        (i  , j+1),
        (i-1, j+1),
        (i-1, j  ),
        (i-1, j-1),
        (i  , j-1),
        (i+1, j-1),
        (i+1, j  ),
        (i+1, j+1),
    ]                               # some of the index pairs may lie outside
                                    # the 10x10 grid
    adjacent_indices = []
    for k, l in naive_adjacent_indices:
        if k in range(n_rows) and l in range(n_cols):
            adjacent_indices.append((k,l))

    return adjacent_indices

def increment(index_list):
    global grid

    for i,j in index_list:
        grid[i,j] += 1

def increment_all():
    global grid

    grid += 1               # each entry of grid is incremented

def one_step_full_energy_to_NaN():
    """
    Alter the entries of grid to NaN where there is enough energy. Increase energy of the adjacent entries by 1.

    Return 1 if anything was changed. Otherwise return 0.
    """

    global grid

    something_changed = 0

    for i in range(n_rows):
        for j in range(n_cols):
            if grid[i,j] > 9:
                grid[i,j] = np.nan
                increment(adjacent_indices(i,j))
                something_changed = 1

    return something_changed

def full_energy_to_NaN():
    global grid
    n_calls = 0             # count how often the helper function was called
    while(one_step_full_energy_to_NaN()):
        n_calls += 1
        # print(n_calls)
    return(n_calls)

def flash(print_grid=False):
    """
    Set all the entries with high energy (i.e. with NaN energy) to zero again. (I.e. emulate a flashing.)

    If optional parameter print_grid is set to True, then the grid is printed. Flashing octopuses are highlighted in yellow color.

    Returns the number of flashing octopuses.
    """
    global grid
    n_flashes = 0

    for i in range(n_rows):
        for j in range(n_cols):
            if np.isnan(grid[i,j]):
                n_flashes += 1
                grid[i,j] = 0

    if (print_grid):
        # a grid point has flashed if and only if it is now zero
        for i in range(n_rows):
            for j in range(n_cols):
                energy_level = int(grid[i,j])
                if energy_level == 0:
                    print(
                        colored(energy_level, 'yellow'),
                        end=''
                    )
                else:
                    print(energy_level, end='')
            print()

    return n_flashes


total_n_flashes = 0
for step in range(1, 100 +1):
    increment_all()
    full_energy_to_NaN()

    if step%10:             # is True iff step is not a multiple of 10
        total_n_flashes += flash(print_grid=False)
    else:
        print('After step ', step, ':', sep='')
        total_n_flashes += flash(print_grid=True)
        print('\n', total_n_flashes, '\n\n', sep='', end='')
