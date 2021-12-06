x_position = 0  # not sure if this is still needed in part 2 of the puzzle
y_position = 0  # depth, i.e. counterintuitively orientated
aim        = 0



with open('02-1-input.txt', 'r') as f:  # same input as before
    stri = f.read()

n_iter = 0

aim_was_above_water = False
y_position_was_above_water = False

while stri:
    n_iter += 1

    index_1 = stri.find(' ')
    command = stri[:index_1]

    index_2 = stri.find('\n')
    dist = int( stri[index_1+1:index_2] )

    stri = stri[index_2+1:]

    if (command == 'forward'):
        x_position += dist
        y_position += aim*dist
        if y_position < 0:
            print("!!!!!!!!!!!!!!!!!!!\nNow we're is flying over the water.")
            y_position_was_above_water = True
    if (command == 'down'):
        aim += dist
    if (command == 'up'):
        aim -= dist
        if aim < 0:
            print("!!!!!!!!!!!!!!!!!!!\nNow aim is flying over the water.")
            aim_was_above_water = True

    print(n_iter, ': x=', x_position, '\ty=', y_position, '\taim=', aim, sep='')

print('----------')
print('final position: x=', x_position, '\ty=', y_position, '\taim=', aim, sep='')
print('x*y=', x_position*y_position, sep='')

print('----------')
print('aim_was_above_water?', aim_was_above_water)
print('y_position_was_above_water?', y_position_was_above_water)
