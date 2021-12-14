with open('14-1-sample_input.txt', 'r') as f:
    stri = f.read()

index = stri.find('\n')
polymer_template = stri[0:index]
stri = stri[index+2:]

insertion_rules = {}
occurences      = {}
while(stri):
    left                  = stri[0]
    right                 = stri[1]
    letter_pair           = stri[0:2]
    inserted              = stri[6]
    insertion_rules[letter_pair] = inserted

    occurences[left]      = 0
    occurences[right]     = 0

    stri                  = stri[8:]

def recursive(left, right, depth):
    if depth == 23:
        print(left, end='')
        occurences[left] += 1
    else:
        # assert(depth < 1)
        inserted = insertion_rules[left + right]

        recursive(left, inserted, depth+1)
        recursive(inserted, right, depth+1)

recursive('N', 'N', 0)
recursive('N', 'C', 0)
recursive('C', 'B', 0)

print('B', end='\n')
occurences['B'] += 1

print(occurences)
max = max(occurences.values())
min = min(occurences.values())
print('Puzzle solution is ', max, '-', min, ' = ', max-min, sep='')
