import pdb  # Python debugger

## Make a list of the lines.
## Each line gives a tuple. First entry is a list with ten entries (the left
## side of |). Second entry is a list with four entries (the right side of |).

with open('08-1-input.txt', 'r') as f:
    stri = f.read()

input_list = []

while(stri):
    patterns_list = []
    for iter in range(10):  # there are ten strings left of |
        index = stri.find(' ')
        pattern = stri[:index]
        patterns_list.append(pattern)

        stri = stri[index+1:]

    assert(stri[0] == '|'), 'While parsing: Could not find | character where expected.'

    stri = stri[2:]         # strip off the '| '

    signals_list = []
    for iter in range(3):   # should be 4, but last string is not terminated by space
        index = stri.find(' ')
        signal = stri[:index]
        signals_list.append(signal)

        stri=stri[index+1:]

    index = stri.find('\n') # last digit of four-digit ouput value
    signal = stri[:index]
    signals_list.append(signal)

    stri = stri[index+1:]


    tup = (patterns_list, signals_list)
    input_list.append(tup)

## Now for part 2 of the puzzle:

segments_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

def intersection(p_1, p_2):
    intersection = ''
    for char in segments_list:
        if char in p_1 and char in p_2:
            intersection = intersection + char
    return intersection

def union(p_1, p_2):
    union = ''
    for char in segments_list:
        if char in p_1 or char in p_2:
            union = union + char
    return union

def symm_diff(p_1, p_2):
    symm_diff = ''
    for char in segments_list:
        if (char in p_1) != (char in p_2):       # xor
            symm_diff = symm_diff + char
    return symm_diff

def n_segments(p):
    return len(p)

def setminus(p_1, p_2):         # here the order of arguments matters
    setminus = ''
    for char in segments_list:
        if (char in p_1) and (char not in p_2):
            setminus = setminus + char
    return setminus

def ordered(p):
    ordered = ''
    for char in segments_list:
        if char in p:
            ordered = ordered + char
    return ordered

def contained(p_1, p_2):         # here the order of arguments matters
    contained = True
    for char in p_1:
        if not char in p_2:
            contained = False
    return contained

# pdb.set_trace()



output_list = []
## The "careful analysis" will be done for each of the entries

for patterns_list, signals_list in input_list:

# pdb.set_trace()

    decoded_patterns = {}

    # find the four easy digits
    for pattern in patterns_list:
        pattern = ordered(pattern)

        if n_segments(pattern) == 2:
            decoded_patterns[pattern] = 1
            one = pattern
        elif n_segments(pattern) == 3:
            decoded_patterns[pattern] = 7
            seven = pattern
        elif n_segments(pattern) == 4:
            decoded_patterns[pattern] = 4
            four = pattern
        elif n_segments(pattern) == 7:
            decoded_patterns[pattern] = 8
            eight = pattern

    # find the digit 3
    for pattern in patterns_list:
        if n_segments(pattern) != 5:    # only interested in patterns with 5 segments
            continue

        # now pattern represents one of the digits 2, 3, and 5.
        pattern = ordered(pattern)
        if contained(one, pattern):
            decoded_patterns[pattern] = 3
            three = pattern

    # find the digit 9
    for pattern in patterns_list:
        if n_segments(pattern) != 6:    # only interested in patterns with 6 segments
            continue

        # now pattern is one of the digits 0, 6, and 9.
        pattern = ordered(pattern)
        if contained(three, pattern):
            decoded_patterns[pattern] = 9
            nine = pattern

    # find the digit 0 and 6
    for pattern in patterns_list:
        if n_segments(pattern) != 6:    # only interested in patterns with 6 segments
            continue

        # now pattern is one of the digits 0, 6, and 9.
        pattern = ordered(pattern)
        if pattern == nine:             # not interested in digit 9 anymore
            continue

        if contained(one, pattern):
            decoded_patterns[pattern] = 0
            zero = pattern
        else:
            decoded_patterns[pattern] = 6
            six = pattern

    # find the digit 2 and 5
    for pattern in patterns_list:
        if n_segments(pattern) != 5:    # only interested in patterns with 5 segments
            continue

        # now pattern is one of the digits 2, 3, and 5.
        pattern = ordered(pattern)
        if pattern == three:            # not interested in digit 3 anymore
            continue

        if contained(pattern, nine):
            decoded_patterns[pattern] = 5
            five = pattern
        else:
            decoded_patterns[pattern] = 2
            two = pattern

    output_value = \
        1000 * decoded_patterns[ordered(signals_list[0])]   \
        + 100 * decoded_patterns[ordered(signals_list[1])]  \
        + 10 * decoded_patterns[ordered(signals_list[2])]   \
        + 1 * decoded_patterns[ordered(signals_list[3])]

    output_list.append(output_value)


print(output_list)

print('Sum of all outputs:', sum(output_list))
