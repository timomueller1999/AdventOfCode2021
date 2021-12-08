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

## Now for part 1 of the puzzle:

count_unique_digits = 0

for _, signals_list in input_list:
    for signal in signals_list:
        if len(signal) in [2,3,4,7]:     # 1 uses 2 segments, 7 uses 3 segments, 4 uses 4 segments, 8 uses 7 segments
            count_unique_digits += 1
            # print(signal)

print(count_unique_digits, 'digits in the ouput with a unique number of segments.')
