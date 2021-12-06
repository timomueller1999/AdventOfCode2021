with open('01-1-input.txt', 'r') as f:  # puzzle input has not changed
    str = f.read()

current_value = 0
last_value    = 0
second_last_value = 0

current_window_sum = 0
last_window_sum    = 0




## get the first three values by hand (without loop)
index = str.find('\n')
second_last_value = int(str[0:index])
str = str[index+1:]

index = str.find('\n')
last_value = int(str[0:index])
str = str[index+1:]

index = str.find('\n')
current_value = int(str[0:index])
str = str[index+1:]

current_window_sum = current_value + last_value + second_last_value
print(current_window_sum, '(N/A - no previous sum)')

## There is nothing to compare, yet.
## So we have to move to the next value.
last_window_sum = current_window_sum
second_last_value = last_value
last_value = current_value




## now the loop
counter = 0

while str != '':

    # get new depth
    index = str.find('\n')
    current_value = int(str[0:index])
    str = str[index+1:]

    # compute window_sum
    current_window_sum = current_value + last_value + second_last_value
    if current_window_sum > last_window_sum:
        counter += 1
        print(current_window_sum, '(increased)', counter)
    elif current_window_sum < last_window_sum:
        print(current_window_sum, '(decreased)')
    else:
        print(current_window_sum, '(no change)')

    # update for next iteration
    last_window_sum = current_window_sum
    second_last_value = last_value
    last_value = current_value
