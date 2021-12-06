x_position = 0
y_position = 0  # depth, i.e. counterintuitively orientated



with open('02-1-input.txt', 'r') as f:
    stri = f.read()

n_iter = 0

while stri:
    n_iter += 1

    index_1 = stri.find(' ')
    command = stri[:index_1]

    index_2 = stri.find('\n')
    dist = int( stri[index_1+1:index_2] )

    stri = stri[index_2+1:]

    if (command == 'forward'):
        x_position += dist
    if (command == 'down'):
        y_position += dist  # y is the depth, i. e. down *increases* y
    if (command == 'up'):
        y_position -= dist
        if y_position < 0:
            print("!!!!!!!!!!!!!!!!!!!\nNow we're flying over the water.")

    print(n_iter, ': x=', x_position, '\ty=', y_position, sep='')

print('----------')
print('final position: x=', x_position, '\ty=', y_position, sep='')
print('x*y=', x_position*y_position, sep='')
