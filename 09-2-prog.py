import numpy as np
import pdb  # Python debugger

with open('09-1-input.txt', 'r') as f:
    stri = f.read()

list_of_lists = []
list = []
while(stri):                        # while not empty string
    height = int( stri[0] )
    list.append(height)
    stri = stri[1:]

    if stri[0] == '\n':              # one full line was read
        list_of_lists.append(list)
        list = []
        stri = stri[1:]             # "delete" the newline character

n_rows = len(list_of_lists)
n_cols = len(list_of_lists[0])

# sensibility check
for row_number in range(n_rows):
    assert(len(list_of_lists[row_number]) == n_cols), \
        "The line " + str(row_number) + " doesn't have the same number of entries as line 0."

heightmap = np.array(list_of_lists)
assert(heightmap.shape == (n_rows, n_cols)), "Dimension problem in transformation of heightmap to array."

## Helper functions

def neighbours(i,j):
    assert(i in range(0, n_rows)), "i is either too large or too small."
    assert(j in range(0, n_cols)), "j is either too large or too small."

    if i==0:
        if j==0:
            return heightmap[1,0], heightmap[0,1]
        elif j==n_cols-1:
            return heightmap[0,n_cols-2], heightmap[1,n_cols-1]
        else:
            return heightmap[0,j-1], heightmap[0,j+1], heightmap[1,j]
    elif i==n_rows-1:
        if j==0:
            return heightmap[n_rows-2,0], heightmap[n_rows-1,1]
        elif j==n_cols-1:
            return heightmap[n_rows-1,n_cols-2], heightmap[n_rows-2,n_cols-1]
        else:
            return heightmap[n_rows-1,j-1], heightmap[n_rows-1,j+1], heightmap[n_rows-2,j]
    else:
        if j==0:
            return heightmap[i-1,0], heightmap[i+1,0], heightmap[i,1]
        elif j==n_cols-1:
            return heightmap[i-1,n_cols-1], heightmap[i+1,n_cols-1], heightmap[i,n_cols-2]
        else:
            return heightmap[i-1,j], heightmap[i+1,j], heightmap[i,j-1], heightmap[i,j+1]

def neighbour_indices(i,j):
    assert(i in range(0, n_rows)), "i is either too large or too small."
    assert(j in range(0, n_cols)), "j is either too large or too small."

    if i==0:
        if j==0:
            return (1,0), (0,1)
        elif j==n_cols-1:
            return (0,n_cols-2), (1,n_cols-1)
        else:
            return (0,j-1), (0,j+1), (1,j)
    elif i==n_rows-1:
        if j==0:
            return (n_rows-2,0), (n_rows-1,1)
        elif j==n_cols-1:
            return (n_rows-1,n_cols-2), (n_rows-2,n_cols-1)
        else:
            return (n_rows-1,j-1), (n_rows-1,j+1), (n_rows-2,j)
    else:
        if j==0:
            return (i-1,0), (i+1,0), (i,1)
        elif j==n_cols-1:
            return (i-1,n_cols-1), (i+1,n_cols-1), (i,n_cols-2)
        else:
            return (i-1,j), (i+1,j), (i,j-1), (i,j+1)

def is_low_point(i,j):
    assert(i in range(0, n_rows)), "i is either too large or too small."
    assert(j in range(0, n_cols)), "j is either too large or too small."

    min_neighbour = min(neighbours(i,j))
    if min_neighbour <= heightmap[i,j]:         # not sure about this equality ...
                                                # but then trial and erros showed that
                                                # the equality is meant to be here
        return False
    elif min_neighbour > heightmap[i,j]:
        return True
    elif min_neighbour == heightmap[i,j]:
        raise

def risk_level(i,j):
    assert(i in range(0, n_rows)), "i is either too large or too small."
    assert(j in range(0, n_cols)), "j is either too large or too small."

    return heightmap[i,j] + 1

def basin(i,j):
    assert(i in range(0, n_rows)), "i is either too large or too small."
    assert(j in range(0, n_cols)), "j is either too large or too small."
    assert(heightmap[i,j]<9), "This spot is a 9."

    basin_indices = [(i,j)]
    list_changed  = True
    while(list_changed):
        list_changed = False
        temp_basin_indices = basin_indices
        for i,j in basin_indices:
            for k,l in neighbour_indices(i,j):
                if heightmap[k,l] < 9 and (k,l) not in temp_basin_indices:
                    temp_basin_indices.append((k,l))
                    list_changed = True
        basin_indices = temp_basin_indices

    return basin_indices

## The actual main

basin_sizes = []
for i in range(n_rows):
    for j in range(n_cols):
        if is_low_point(i,j):
            basin_size = len(basin(i,j))
            basin_sizes.append(basin_size)

print('All basin sizes:', basin_sizes)

prod = 1
for iter in range(3):
    factor = max(basin_sizes)
    print("Multiply by basin size", factor)
    prod *= factor
    basin_sizes.remove(factor)

print("Product:", prod)
