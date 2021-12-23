import numpy as np
import pdb  # Python debugger

with open('22-1-input.txt', 'r') as f:
    stri = f.read()

min_val = -50
max_val = 50

commands = []

while(stri):
    index   = stri.find(' ')
    command = stri[:index]
    stri    = stri[index+3:]

    index   = stri.find('.')
    x_min   = int(stri[:index])
    stri    = stri[index+2:]

    index   = stri.find(',')
    x_max   = int(stri[:index])
    stri    = stri[index+3:]

    index   = stri.find('.')
    y_min   = int(stri[:index])
    stri    = stri[index+2:]

    index   = stri.find(',')
    y_max   = int(stri[:index])
    stri    = stri[index+3:]

    index   = stri.find('.')
    z_min   = int(stri[:index])
    stri    = stri[index+2:]

    index   = stri.find('\n')
    z_max   = int(stri[:index])
    stri    = stri[index+1:]

    assert(x_min <= x_max)
    assert(y_min <= y_max)
    assert(z_min <= z_max)

    if command == 'on':
        set_to = 1
    elif command == 'off':
        set_to = 0
    else:
        raise ValueError

    if (min_val <= x_min and min_val <= y_min and min_val <= z_min and x_max <= max_val and y_max <= max_val and z_max <= max_val):
        commands.append(
            (set_to, x_min-min_val, 1+x_max-min_val, y_min-min_val, 1+y_max-min_val, z_min-min_val, 1+z_max-min_val)
        )

print('Finished parsing')

grid = np.zeros(
    shape = (1+max_val-min_val, 1+max_val-min_val, 1+max_val-min_val),
    dtype = int
)

for set_to, x_min, x_max, y_min, y_max, z_min, z_max in commands:
    grid[x_min:x_max, y_min:y_max, z_min:z_max] = set_to

n_ones = grid.sum()

print('Number of cubes turned on:', n_ones)
