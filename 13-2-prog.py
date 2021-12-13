import pdb  # Python debugger
import numpy as np

with open('13-1-input.txt', 'r') as f:
    stri = f.read()

## parsing
x_max = 0
y_max = 0
dots = []
while stri[0] != '\n':              # end of dots section in the input is
                                    # characterized by a double newline
    index_1 = stri.find(',')
    index_2 = stri.find('\n')

    x = int(stri[0         : index_1])
    y = int(stri[index_1+1 : index_2])

    if (x > x_max):
        x_max = x
    if (y > y_max):
        y_max = y

    dots.append( (x,y) )

    stri = stri[index_2+1 :    ]


stri = stri[1:]         # throw away the newline character
assert(stri[0:10] == 'fold along'), 'Expected the line "fold along"'
folds = []

while stri != '':                   # end of fold instructions is characterized
                                    # by the input ending
    axis = stri[11]
    stri = stri[13:]

    index = stri.find('\n')
    value = int( stri[ : index] )
    stri  = stri[index+1 : ]

    folds.append( (axis, value) )

x_max += 1
y_max += 1
print('Found x_max =', x_max, 'and y_max =', y_max)


def show(trans_paper: np.ndarray):
    x_max, y_max = trans_paper.shape
    for y in range(y_max):
        for x in range(x_max):
            print('#' if trans_paper[x,y] else ' ' , end='')
        print()
    print()

def fold(
    trans_paper: np.ndarray,
    axis: str,
    value: int,
):
    x_max, y_max = trans_paper.shape
    if (axis == 'x'):
        assert(value >= x_max // 2), 'Fold will extend the paper to the left.'
        return_paper = np.zeros( (value, y_max) )

        for delta_x in range(1, value+1):
            for y in range(y_max):
                if trans_paper[value-delta_x, y] or trans_paper[value+delta_x, y]:
                    return_paper[value-delta_x, y] = 1

        return return_paper

    elif (axis == 'y'):
        assert(value >= y_max // 2), 'Fold will extend the paper over the top.'
        return_paper = np.zeros( (x_max, value) )

        for x in range(x_max):
            for delta_y in range(1, value+1):
                if trans_paper[x, value-delta_y] or trans_paper[x, value+delta_y]:
                    return_paper[x, value-delta_y] = 1

        return return_paper

    else:
        raise ValueError('Expected axis to be "x" or "y".')

def n_dots(trans_paper: np.ndarray):
    return int(trans_paper.sum())


## initialize transparency paper:
trans_paper = np.zeros((x_max, y_max))
for x,y in dots:
    trans_paper[x,y] = 1

show(trans_paper)

for axis, value in folds:
    trans_paper = fold(trans_paper, axis, value)
    show(trans_paper)
    print('Number of dots (although not necessary for part two):', n_dots(trans_paper), end='\n\n')
