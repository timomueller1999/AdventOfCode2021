import pdb  # Python debugger

with open('10-1-input.txt', 'r') as f:
    stri = f.read()

## Stack class from the internet:
class Stack:

    def __init__(self):
        """
        Initializing Stack.
        """
        self.stack = []

    def isEmpty(self) -> bool:
        return True if len(self.stack) == 0 else False

    def length(self) -> int:
        return len(self.stack)

    def top(self) -> str:
        return self.stack[-1]

    def push(self, x: str) -> None:
        assert(len(x) == 1), 'Stack.push() can only handle one-character strings.'
        self.x = x
        self.stack.append(x)

    def pop(self) -> str:
        return self.stack.pop()


## My own code:
illegal_character_score  = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}
parenthesis_matches_dict = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}
parenthesis_matches_list = ['()', '[]', '{}', '<>']
parenthesis_memory = Stack()

syntax_error_score = 0

# pdb.set_trace()

while(stri):
    parsing_is_fine = True
    while(stri[0] != '\n'):
        new_parenthesis = stri[0]
        stri = stri[1:]

        if new_parenthesis in ['(', '[', '{', '<']:
            parenthesis_memory.push(new_parenthesis)
        elif new_parenthesis in [')', ']', '}', '>']:
            last_open = parenthesis_memory.pop()
            match = last_open + new_parenthesis
            if match in parenthesis_matches_list:
                continue
            else:
                # parenthesis mismatch: input line is corrupted
                parsing_is_fine = False

                print('Expected ' + parenthesis_matches_dict[last_open]
                    + ' but found ' + new_parenthesis + ' instead.')

                # add to syntax error score
                syntax_error_score += illegal_character_score[new_parenthesis]

                # flush the line; only newline character remains
                index = stri.find('\n')
                stri = stri[index:]
                break
        else:
            raise ValueError('Expecting one of (,),[,],{,},<,>; but received '
                + new_parenthesis)

    if parsing_is_fine:
        if parenthesis_memory.isEmpty():
            print('Line was parsed correctly.')     # according to puzzle, this should not happen
        else:
            print('Line is incomplete.')

    stri = stri[1:]                 # get rid of the newline character in front

print('The syntax error score is', syntax_error_score)
