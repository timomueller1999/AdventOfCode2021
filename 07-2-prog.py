import numpy as np

## There will only be one alteration to the previous solution: After the
## distance matrix of shape (max_pos, n_crabs) is determined, its entries
## are taken by the function
## f: N \to N, n \mapsto \sum_{i=0}^n i
## This reflects the actual fuel cost that a journey of distance n needs.

def sum_up_to(n):
    return (n*(n+1)) // 2  # Gauß' formula for \sum_{i=0}^n i

with open('07-1-input.txt', 'r') as f:
    stri = f.read()

positions_list = []
while stri:
    index = stri.find(',')     # if no comma exists, then index = -1
    pos   = int( stri[0:index])# if no comma existed, this line works
    positions_list.append(pos)
    if index == -1:
        stri = ''
    else:
        stri  = stri[index+1:]  # this would be stri = stri if index = -1

positions_array = np.array(positions_list).reshape((1,-1))  # row vector
n_crabs = positions_array.shape[1]
max_pos = np.max(positions_array)
assert(np.min(positions_array) >= 0), 'There is a negative position in the input'

print('Number of crabs:', n_crabs)
print('Maximum position:', max_pos)


distances = np.zeros((max_pos, n_crabs)).astype(int)
for pos in range(max_pos):
    distances[pos, :] = pos

distances = distances - positions_array # positions_array broadcasted to shape
                                        # (max_pos, n_crabs)

distances = np.abs(distances)           # now distances[i,j] contains the
                                        # positive distance of crab j to
                                        # position i

distances = sum_up_to(distances)        # element-wise application of the
                                        # function

accum_distance = np.sum(distances, axis=1, keepdims=True)
                                        # contains, for each position pos, the
                                        # total fuel cost for the crabs to
                                        # align in that position;
                                        # accum_distance is a column vector

best_pos = np.argmin(accum_distance)
best_cost = np.min(accum_distance)

print('Best position to align:', best_pos)
print('This needs', best_cost, 'fuel units.')

assert(accum_distance[best_pos] == best_cost), 'Logical error'
