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

    elif np.abs(x_2 - x_1) == np.abs(y_2 - y_1):
        print('\tcovers')

        y_ascending = True if y_2 - y_1 >= 0 else False  # case ==0 does not occur
        x_ascending = True if x_2 - x_1 >= 0 else False  # case ==0 does not occur

        current_x   = x_1
        current_y   = y_1

        field[current_x, current_y] += 1
        print('\t\t', current_x, current_y)

        while(True):
            if x_ascending:
                current_x += 1
            else:
                current_x -= 1

            if y_ascending:
                current_y += 1
            else:
                current_y -= 1

            field[current_x, current_y] += 1
            print('\t\t', current_x, current_y)

            if current_x == x_2:
                assert(current_y == y_2), 'Logical error in diagonal'
                break



    # elif x_2 - x_1 == y_2 - y_1:  # diagonal line in the "intuitive" direction
    #     print('\tcovers')
    #     d = x_2 - x_1
    #     if d >= 0:
    #         for i in range(d+1):
    #             field[x_1 + i, y_1 + i] += 1
    #             print('\t\t', x_1 + i, y_1 + i)
    #             # pdb.set_trace()
    #     elif d <= 0:
    #         for i in range(-d+1):
    #             field[x_2 + i, y_2 + i] += 1
    #             print('\t\t', x_2 + i, y_2 + i)
    #             # pdb.set_trace()
    # elif x_2 - x_1 == y_1 - y_2:  # diagonal line in the "counterintuitive" direction
    #     print('\tcovers')
    #     d = x_2 - x_1
    #     if d >= 0:
    #         for i in range(d+1):
    #             field[x_1 + i, y_2 + i] += 1
    #             print('\t\t', x_1 + i, y_2 + i)
    #     elif d > 0:
    #         for i in range(-d+1):
    #             field[x_2 + i, y_1 + i] += 1
    #             print('\t\t', x_2 + i, y_1 + i)


# final computations:
dangerous = np.where(field > 1, 1, 0)
n_dangerous = dangerous.sum()

# print(field.T)  # transpose so that the view is similar as in the puzzle
# print(dangerous.T)  # transpose so that the view is similar as in the puzzle

print('--------------------')
print('Number of dangerous spots:', n_dangerous)
