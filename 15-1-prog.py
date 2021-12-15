import numpy as np
import pdb  # Python debugger

with open('15-1-input.txt') as f:
    stri = f.read()


list_of_lines = []
list_of_risks = []

while(stri):
    list_of_risks = []

    while(stri[0] != '\n'):
        list_of_risks.append( int( stri[0] ) )
        stri = stri[1:]
    list_of_lines.append(list_of_risks)
    stri = stri[1:]

y_max = len(list_of_lines)              # the horizontal extension of cave
x_max = len(list_of_risks)              # the vertical extension of cave
max_risk_level = 10*(x_max + y_max)     # in the end, every spot in the cavern
                                        # will have a lower risk level than this

cavern = np.zeros( (y_max, x_max) )     # correctly ordered
risk_levels = np.ones( (y_max, x_max ))
risk_levels *= max_risk_level
risk_levels[0,0] = 0                    # no danger on the field where we start

print(y_max, x_max)

for y in range(y_max):
    list_of_risks = list_of_lines.pop(0)
    for x in range(x_max):
        cavern[y,x] = list_of_risks.pop(0)
        stri = stri[1:]
    assert(not list_of_risks), 'Error while parsing: list_of_risks was not empty'
assert(not list_of_lines), 'Error while parsing: list_of_lines was not empty'

print(cavern)
print(risk_levels)

## helper functions
def neighbours(i,j):
    assert(i in range(0, y_max)), "i is either too large or too small."
    assert(j in range(0, x_max)), "j is either too large or too small."

    if i==0:
        if j==0:
            return risk_levels[1,0], risk_levels[0,1]
        elif j==x_max-1:
            return risk_levels[0,x_max-2], risk_levels[1,x_max-1]
        else:
            return risk_levels[0,j-1], risk_levels[0,j+1], risk_levels[1,j]
    elif i==y_max-1:
        if j==0:
            return risk_levels[y_max-2,0], risk_levels[y_max-1,1]
        elif j==x_max-1:
            return risk_levels[y_max-1,x_max-2], risk_levels[y_max-2,x_max-1]
        else:
            return risk_levels[y_max-1,j-1], risk_levels[y_max-1,j+1], risk_levels[y_max-2,j]
    else:
        if j==0:
            return risk_levels[i-1,0], risk_levels[i+1,0], risk_levels[i,1]
        elif j==x_max-1:
            return risk_levels[i-1,x_max-1], risk_levels[i+1,x_max-1], risk_levels[i,x_max-2]
        else:
            return risk_levels[i-1,j], risk_levels[i+1,j], risk_levels[i,j-1], risk_levels[i,j+1]

def update_risk_levels() -> bool:
    """
    Work on the array risk_levels and update, where possible, to lower risk levels. Return whether a change was made.
    """

    made_change = False
    for y in range(y_max):
        for x in range(x_max):
            min_neighbour_risk = min(neighbours(y,x))
            if (min_neighbour_risk + cavern[y,x] < risk_levels[y,x]):
                risk_levels[y,x] = min_neighbour_risk + cavern[y,x]
                made_change = True
    return made_change

step=0
while(update_risk_levels()):
    step += 1
    print('After', step, 'steps:')
    print(risk_levels)

print('Least possible risk level:', risk_levels[y_max-1, x_max-1])
