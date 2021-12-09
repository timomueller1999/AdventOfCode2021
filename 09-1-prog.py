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


## The actual main

sum_risk_levels = 0
for i in range(n_rows):
    for j in range(n_cols):
        if is_low_point(i,j):
            sum_risk_levels += risk_level(i,j)

print("Sum of all risk levels:", sum_risk_levels)

print(n_rows)
print(n_cols)
