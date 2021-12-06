current_list = [1]
day = 0

while (day < 256):
    temp = current_list
    current_list = []

    for fish in temp:
        if fish == 0:
            current_list.append(6)
            current_list.append(8)
        elif fish > 0:
            current_list.append(fish-1)
    # print('After\t', day, 'days:', current_list)
    print('Number of fish after', day, 'days:', len(current_list))

    day += 1

print('In the end: Number of fish:', len(current_list))
