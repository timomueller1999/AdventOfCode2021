liste = []
with open('01-1-input.txt') as f:
    str = f.read()

# print(str)

first_time = True
temp_1 = 0
temp_2 = 0
counter = 0

while str != '':
    index = str.find('\n')
    temp_2 = int(str[0:index])

    print(temp_2, end='\t')

    if first_time:
        print('N/A no preceding depth', counter)
    else:
        if temp_2 > temp_1:
            counter += 1
            print('increasing', counter)
        elif temp_2 < temp_1:
            print('decreasing')
        else:
            print('!!!!! UNEXPECTED !!!!! temp_2 =', temp_2)

    first_time = False
    str = str[index+1:]
    temp_1 = temp_2
