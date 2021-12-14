import pdb  # Python debugger


with open('14-1-input.txt', 'r') as f:
    stri = f.read()

index = stri.find('\n')
polymer_template = stri[0:index]
stri = stri[index+2:]

insertion_rules  = {}
occurences_pairs = {}
occurences_pairs_temp = {}
occurences       = {}       # for number of occurences of each letter
letter_pairs = []
letters = []
while(stri):
    left                  = stri[0]
    right                 = stri[1]
    letter_pair           = stri[0:2]
    inserted              = stri[6]
    insertion_rules[letter_pair]  = inserted

    occurences[left] = 0
    occurences[right] = 0                   # initialize the keys of occurences
    letters.append(left)
    letters.append(right)

    occurences_pairs[letter_pair] = 0       # initialize the keys of occurences_pairs
    occurences_pairs_temp[letter_pair] = 0
    letter_pairs.append(letter_pair)

    stri                  = stri[8:]

# initialize values of occurences_pairs
for index in range(len(polymer_template) -1):
    letter_pair = polymer_template[index:index+2]
    occurences_pairs[letter_pair] += 1

# pdb.set_trace()


for step in range(1, 41):

    # prepare temporal dictionary for use
    for letter_pair in letter_pairs:
        occurences_pairs_temp[letter_pair] = 0

    # pdb.set_trace()

    # iteration step:
    for letter_pair in letter_pairs:
        left = letter_pair[0]
        right = letter_pair[1]
        inserted = insertion_rules[letter_pair]

        occurences_pairs_temp[left + inserted] += occurences_pairs[letter_pair]
        occurences_pairs_temp[inserted + right] += occurences_pairs[letter_pair]

    # pdb.set_trace()

    occurences_pairs = occurences_pairs_temp.copy()

    print('After', step, 'steps:\n', occurences_pairs)


# Go back from pairs of letters to single letters. For this, count only the left
# letter of each pair. In the end, we have to add the rightmost letter of the
# input once.

for letter_pair in letter_pairs:
    left = letter_pair[0]
    occurences[left] += occurences_pairs[letter_pair]

rightmost = polymer_template[-1]
occurences[rightmost] += 1

print('Result:', occurences, sep='\n')

max = max(occurences.values())
min = min(occurences.values())

print('Puzzle solution is ', max, '-', min, ' = ', max-min, sep='')
