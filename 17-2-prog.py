import math
import numpy as np
import pdb  # Python debugger


## Today, I type the input manually instead of writing a parse function.

# The target area:
## Sample input:
# x_min = 20
# x_max = 30
# y_min = -10
# y_max = -5

x_min = 143
x_max = 177
y_min = -106
y_max = -71


# Some very rough estimations:
max_n_steps      = x_max+50
min_start_x_velo = 1
max_start_x_velo = x_max+50
min_start_y_velo = y_min-50
max_start_y_velo = math.ceil( y_max/x_max + (x_max-1)/2 ) + 400
        # The idea for max_start_y_velo is: "If, after x_max steps, the
        # y-coordinate is still >y_max, then the start velocity in y-direction
        # was too high."

def in_target_area(x,y):
    return x in range(x_min, x_max+1) and y in range(y_min, y_max+1)

global_max_y_pos = 0
n_initial_velos = 0

for start_x_velo in range(min_start_x_velo, max_start_x_velo+1):
    for start_y_velo in range(min_start_y_velo, max_start_y_velo+1):
        x_velo  = start_x_velo
        y_velo  = start_y_velo
        x_pos   = 0
        y_pos   = 0
        n_steps = 0

        max_y_pos = 0

        while(x_pos <= x_max and n_steps <= max_n_steps):


            x_pos += x_velo
            y_pos += y_velo
            max_y_pos = max(y_pos, max_y_pos)

            if x_velo > 0:
                x_velo -= 1
            elif x_velo < 0:
                x_velo += 1

            y_velo -= 1

            n_steps += 1

            if in_target_area(x_pos, y_pos):
                print('---------------------------------')
                print('SUCCESS')
                print('Start x-velocity:  ', start_x_velo)
                print('Start y-velocity:  ', start_y_velo)
                print('Num ber of steps:  ', n_steps)
                print('Reached x-position:', x_pos)
                print('Reached y-position:', y_pos)
                print('Maximum reached y: ', max_y_pos)

                global_max_y_pos = max(global_max_y_pos, max_y_pos)
                n_initial_velos += 1
                break

print('Maximum reached y-position overall:', global_max_y_pos)
print('Number of initial velociteis:', n_initial_velos)
