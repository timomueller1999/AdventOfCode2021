import pdb  # Python debugger
import numpy as np

with open('05-1-input.txt', 'r') as f:
    stri = f.read()

vent_list = []
x_max = 1000
y_max = 1000

while (stri):
    index = stri.find(',')
    x_1   = int( stri[:index] )
    stri  = stri[index+1:]

    index = stri.find(' ')
    y_1   = int( stri[:index] )
    stri  = stri[index+4:]

    index = stri.find(',')
    x_2   = int( stri[:index] )
    stri  = stri[index+1:]

    index = stri.find('\n')
    y_2   = int( stri[:index] )
    stri  = stri[index+1:]

    assert(x_1 < x_max), 'x_1 zu groß:' + str(x_1)
    assert(x_2 < x_max), 'x_2 zu groß:' + str(x_2)
    assert(x_1 >= 0),    'x_1 negativ:' + str(x_1)
    assert(x_1 >= 0),    'x_2 negativ:' + str(x_2)

    assert(y_1 < y_max), 'y_1 zu groß:' + str(y_1)
    assert(y_2 < y_max), 'y_2 zu groß:' + str(y_2)
    assert(y_1 >= 0),    'y_1 negativ:' + str(y_1)
    assert(y_1 >= 0),    'y_2 negativ:' + str(y_2)

    vent_list.append((x_1, y_1, x_2, y_2))

# pdb.set_trace()


# initialize the field:
field = np.zeros((x_max, y_max))

# marker the vents:
for tup in vent_list:
    x_1, y_1, x_2, y_2 = tup

    print('Entry', x_1, y_1, x_2, y_2)

    if x_1 == x_2:  # vertical line
        print('\tcovers')
        for y in range(np.minimum(y_1, y_2), np.maximum(y_1, y_2)+1):
            field[x_1, y] += 1
            print('\t\t', x_1, y)
    elif y_1 == y_2:  # horizontal line
        print('\tcovers')
        for x in range(np.minimum(x_1, x_2), np.maximum(x_1, x_2)+1):
            field[x, y_1] += 1
            print('\t\t', x, y_1)

# final computations:
dangerous = np.where(field > 1, 1, 0)
n_dangerous = dangerous.sum()

print(field)

print(dangerous)

print(n_dangerous)
