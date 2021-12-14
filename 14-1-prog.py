with open('14-1-input.txt', 'r') as f:
    stri = f.read()

index = stri.find('\n')
polymer_template = stri[0:index]
stri = stri[index+2:]

insertion_rules = {}
while(stri):
    letter_pair           = stri[0:2]
    inserted              = stri[6]
    insertion_rules[letter_pair] = inserted

    stri                  = stri[8:]

for step in range(1, 11):

    temp = ''
    leng = len(polymer_template)

    for index in range(leng - 1):
        letter_pair = polymer_template[index: index+2]
        inserted = insertion_rules[letter_pair]
        left = polymer_template[index]
        right = polymer_template[index+1]

        temp = temp + left + inserted

    temp += polymer_template[-1]

    polymer_template = temp
    print('After step ', step, ': ', polymer_template, sep='')

occurences = {}
for letter in polymer_template:
    if letter in occurences.keys():
        occurences[letter] += 1
    else:
        occurences[letter] = 1

print(occurences)

max_occurence = max(occurences.values())
min_occurence = min(occurences.values())
puz_solution  = max_occurence - min_occurence

print('Puzzle solution is ', max_occurence, '-', min_occurence, ' = ', puz_solution)
