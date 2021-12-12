import pdb  # Python debugger
import string

with open('12-1-input.txt', 'r') as f:
    stri = f.read()

caves = set()
connected_caves_dict = {}        # will store, for each cave, the set of adjacent caves

while (bool(stri)):
    index_1 = stri.find('-')
    cave_1  = stri[0:index_1]
    index_2 = stri.find('\n')
    cave_2  = stri[index_1 + 1: index_2]

    stri    = stri[index_2 + 1: ]

    caves.add(cave_1)
    caves.add(cave_2)

    if (cave_1 in connected_caves_dict.keys()):
        connected_caves_dict[cave_1].add(cave_2)
    else:
        connected_caves_dict[cave_1] = {cave_2}

    if (cave_2 in connected_caves_dict.keys()):
        connected_caves_dict[cave_2].add(cave_1)
    else:
        connected_caves_dict[cave_2] = {cave_1}



## helper functions

def is_big_cave(cave: str):
    return cave[0] in string.ascii_uppercase

def is_small_cave(cave: str):
    return cave[0] in string.ascii_lowercase

def is_finished_path(path: list):
    return path[-1] == 'end'

def contains_a_small_cave_twice(path: list):
    return_val = False
    for cave in path:
        if (is_small_cave(cave)):
            if path.count(cave) >= 2:           # logically, this can only be ==
                return_val = True
    return return_val

def extend_path(partial_path: list):
    """
    For a given path through the cave system, return the set of all possible extensions of this path by one step, together with a bool value indicating whether new paths were found in this step.
    """

    extended_paths = []
    found_new_path = False
    last_cave = partial_path[-1]

    if (last_cave == 'end'):        # The path should not be continued
        return [partial_path]

    for connected_cave in connected_caves_dict[last_cave]:
        if (is_big_cave(connected_cave)):           # big caves are always OK
            extended_paths.append(partial_path + [connected_cave])
            found_new_path = True
        elif connected_cave not in partial_path:    # small caves that have not
                                                    # occured before are always OK
            extended_paths.append(partial_path + [connected_cave])
            found_new_path = True
        elif connected_cave == 'start':             # 'start' must not be visited
                                                    # again
            continue
        elif not contains_a_small_cave_twice(partial_path):
                                                    # small caves that have occured
                                                    # before are still OK, if
                                                    # no other cave occures
                                                    # twice
            extended_paths.append(partial_path + [connected_cave])
            found_new_path = True

    return extended_paths, found_new_path

def extend_paths(
    partial_paths: list,        # list of lists
):
    extended_paths = []
    found_new_path = False
    for path in partial_paths:
        if not is_finished_path(path):
            new_paths, found_new = extend_path(path)
            extended_paths += new_paths
            if (found_new):
                found_new_path = True
        else:
            extended_paths.append(path)

    return extended_paths, found_new_path


## compute all paths:
current_paths = [['start']]
found_new_path = True
while(found_new_path):
    current_paths, found_new_path = extend_paths(current_paths)

## print all paths:
for path in current_paths:
    print(path)

## result:
print('Number of possible paths:', len(current_paths))
