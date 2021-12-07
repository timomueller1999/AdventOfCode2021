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
                self.won_last_num = last_num

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





test_numbers = np.array([[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20], [21,22,23,24,25]])
test_board = Bingo_Board(test_numbers)

test_board.print_board()

pdb.set_trace()
