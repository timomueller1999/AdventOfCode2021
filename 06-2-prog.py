import pdb  # Python debugger

# dict_num[k] == number of fish that one lanternfish, initialized as k, produces within 128 days
# dict_list[k] == the list of these fish

dict_num_128  = {}
dict_list_128 = {}

for k in range(9):
    current_list = [k]
    day = 0

    while (day < 128):
        temp = current_list
        current_list = []

        for fish in temp:
            if fish == 0:
                current_list.append(6)
                current_list.append(8)
            elif fish > 0:
                current_list.append(fish-1)
        # print('After\t', day, 'days:', current_list)
        # print('Number of fish:', len(current_list))

        day += 1

    print('Started with k=', k, ', in the end had ', len(current_list), ' fish.', sep='')
    dict_num_128[k]  = len(current_list)
    dict_list_128[k] = current_list

# pdb.set_trace()


input = [5,3,2,2,1,1,4,1,5,5,1,3,1,5,1,2,1,4,1,2,1,2,1,4,2,4,1,5,1,3,5,4,3,3,
1,4,1,3,4,4,1,5,4,3,3,2,5,1,1,3,1,4,3,2,2,3,1,3,1,3,1,5,3,5,1,3,1,4,2,1,4,1,5,
5,5,2,4,2,1,4,1,3,5,5,1,4,1,1,4,2,2,1,3,1,1,1,1,3,4,1,4,1,1,1,4,4,4,1,3,1,3,4,
1,4,1,2,2,2,5,4,1,3,1,2,1,4,1,4,5,2,4,5,4,1,2,1,4,2,2,2,1,3,5,2,5,1,1,4,5,4,3,
2,4,1,5,2,2,5,1,4,1,5,1,3,5,1,2,1,1,1,5,4,4,5,1,1,1,4,1,3,3,5,5,1,5,2,1,1,3,1,
1,3,2,3,4,4,1,5,5,3,2,1,1,1,4,3,1,3,3,1,1,2,2,1,2,2,2,1,1,5,1,2,2,5,2,4,1,1,2,
4,1,2,3,4,1,2,1,2,4,2,1,1,5,3,1,4,4,4,1,5,2,3,4,4,1,5,1,2,2,4,1,1,2,1,1,1,1,5,
1,3,3,1,1,1,1,4,1,2,2,5,1,2,1,3,4,1,3,4,3,3,1,1,5,5,5,2,4,3,1,4]

n_fish_256 = 0
n_considered_fish = 0
for fish in input:
    list_128 = dict_list_128[fish]
    for fish_128 in list_128:
        n_fish_256 += dict_num_128[fish_128]
    n_considered_fish += 1
    print('After ', n_considered_fish, ' considered: ', n_fish_256)
