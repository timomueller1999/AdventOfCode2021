import numpy as np
import pdb  # Python debugger

with open('22-2-sample_input.txt', 'r') as f:
    stri = f.read()

min_val = -50
max_val = 50

set_tos= []     # only word 'on' or 'off'
x_mins = []
x_maxs = []
y_mins = []
y_maxs = []
z_mins = []
z_maxs = []

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

    set_tos.append(set_to)
    x_mins.append(x_min)
    x_maxs.append(x_max)
    y_mins.append(y_min)
    y_maxs.append(y_max)
    z_mins.append(z_min)
    z_maxs.append(z_max)

print('Finished parsing')

l = len(set_tos)
print('Number of commands:', l)
x_min_val = min(x_mins)
x_max_val = max(x_maxs)
y_min_val = min(y_mins)
y_max_val = max(y_maxs)
z_min_val = min(z_mins)
z_max_val = max(z_maxs)

commands = []

for iter in range(l):
    set_to= set_tos[iter]
    x_min = x_mins[iter]
    x_max = x_maxs[iter]
    y_min = y_mins[iter]
    y_max = y_maxs[iter]
    z_min = z_mins[iter]
    z_max = z_maxs[iter]

    commands.append(
        (set_to, x_min-x_min_val, 1+x_max-x_min_val, y_min-y_min_val, 1+y_max-y_min_val, z_min-z_min_val, 1+z_max-z_min_val)
    )


print('Start initializing grid')

grid = np.zeros(
    shape = (1+x_max_val-x_min_val, 1+x_max_val-x_min_val, 1+x_max_val-x_min_val),
    dtype = bool
)

print('Initialized grid')

for set_to, x_min, x_max, y_min, y_max, z_min, z_max in commands:
    grid[x_min:x_max, y_min:y_max, z_min:z_max] = set_to

n_ones = grid.sum()

print('Number of cubes turned on:', n_ones)
