import numpy as np
from termcolor import colored
import pdb          # Python debugger

class Bingo_Board:
    def __init__(self, numbers, name='generic board name'):
        assert(type(numbers) == np.ndarray), 'Numbers for the board have to be given as an numpy.ndarray of shape (5,5).'
        assert(numbers.shape == (5,5)), 'The given array (which contains the numbers for the board) has to be of shape (5,5).'

        self.marked_color   = 'green'
        self.unmarked_color = 'yellow'

        self.name           = name
        self.board          = numbers
        self.marked         = np.zeros((5,5))
        self.won            = False
        self.won_by_row     = None  # index of row with which the board was won
        self.won_by_col     = None  # index of column with which the board was won
        self.won_last_num   = None
        self.won_last_num   = None  # number that was drawn when the board won

    def mark(self,n):
        if self.won: return None    # no need to mark further fields

        for i in range(5):
            for j in range(5):
                if self.board[i,j] == n:
                    self.marked[i,j] = 1

        self.last_num = n

        return 0                    # success

    def check_won(self):
        """
        Set self.won to True if this board has won.

        Parameters
        ----------
        self:       Instance of Bingo_Board on which the method is called.

        Return
        ------
        None if board had already won before; 0 if board has not won yet; 1 if
        board has just won.

        Behaviour
        ---------
        If this board had already won, nothing happens and None is returned.
        Otherwise, check whether this board has won. If it has won, set the
        parameters self.won to True, self.won_last_num to self.last_num, and set
        self.won_by_row or self.won_by_col to the index of the fully marked row
        or column, respectively.
        """

        if self.won == True: return None

        for i in range(5):  # row number
            if self.marked[i,:].sum() == 5:
                self.won = True
                self.won_by_row = i
                self.won_last_num = self.last_num

                return 1             # no need to also check the columns

        for j in range(5):  # column number
            if self.marked[:,j].sum() == 5:
                self.won = True
                self.won_by_col = j
                self.won_last_num = self.last_num

                return 1

        return 0

    def compute_score(self):
        if self.won == False: return None

        sum_of_unmarked = 0
        for i in range(5):
            for j in range(5):
                if self.marked[i,j] == 0:
                    sum_of_unmarked += self.board[i,j]

        return self.won_last_num * sum_of_unmarked

    def print_board(self):
        print(self.name, ':', sep='')
        for i in range(5):
            for j in range(5):
                if self.marked[i,j]:
                    print( colored(self.board[i,j] , self.marked_color), '\t', sep='', end='' )
                else:
                    print( colored(self.board[i,j] , self.unmarked_color), '\t', sep='', end='' )
            print()                 # prints one newline





with open('04-1-input.txt', 'r') as f:
    stri = f.read()


## parse drawn numbers
numbers_to_draw = []
while(True):
    index = stri.find(',')

    if index==-1:               # now comes the last list element
        index = stri.find('\n')
        n = int( stri[:index] )
        numbers_to_draw.append(n)
        stri = stri[index+1:]   # skip one of the two newlines
        break
    else:                       # everything fine; we are still somewhere inside the list
        n = int( stri[:index] )
        numbers_to_draw.append(n)
        stri = stri[index+1:]

print(numbers_to_draw)
print(stri)

## parse bingo boards
board_number = 0
board_list   = []
while(stri):             # while not empty
    numbers_list = []
    stri = stri[1:]         # skip newline
    for i in range(5):      # row number
        for j in range(5):  # column number
            n = int( stri[:3] )
            numbers_list.append(n)
            stri = stri[3:] # works regardless of whether the third character is a space or a newline

    assert(len(numbers_list) == 25)
    numbers = np.array(numbers_list).reshape((5,5))

    board_number += 1
    board = Bingo_Board(numbers, 'Board ' + str(board_number).zfill(3))
    board_list.append(board)


## begin to draw numbers
n_played_boards = len(board_list)           # number of boards that haven't won
last_board_number = -1

index = 0
while n_played_boards > 1:
    number = numbers_to_draw[index]
    for board in board_list:
        if board.mark(number) is not None:  # board had not won before
            n_played_boards -= board.check_won()        # can not return None because of the preceding if-statement
    print('index =', index)
    print('n_played_boards =', n_played_boards)
    index += 1

assert(n_played_boards == 1), 'All boards won with the same drawn number.'

for board in board_list:
    if board.won:
        continue

    # Now board is the last board that has not won
    while n_played_boards == 1:
        number = numbers_to_draw[index]
        assert(board.mark(number) is not None), 'Something went wrong.'
        if (board.check_won() == 1):
            print('Last board has just won with score', board.compute_score())
            n_played_boards -= 1
        print('index =', index)
        print('n_played_boards =', n_played_boards)
        index += 1
