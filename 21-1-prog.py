import pdb  # Python debugger

board_size = 10
winning_score = 1000

player_1_starting_position = 7  # sample: 4, real input: 7
player_2_starting_position = 3  # sample: 8, real input: 3

class deterministic_die():
    def __init__(self):
        self.next_score = 1
        self.n_rolled   = 0

    def roll(self):
        ret = self.next_score
        self.next_score = self.next_score+1
        if self.next_score == 101:
            self.next_score=1
        self.n_rolled += 1

        return ret

class pawn():
    def __init__(self, starting_space):
        self.space = starting_space
        self.score = 0

    def move_on_board(self, n_spaces, die):
        self.space = (self.space + n_spaces) % board_size
        if self.space == 0:
            self.space = 10

    def take_turn(self, die):
        for iter in range(3):
            n_spaces = die.roll()
            self.move_on_board(n_spaces, die)
        self.score += self.space

    def has_won(self):
        return self.score >= winning_score

pawn_1 = pawn(starting_space = player_1_starting_position)
pawn_2 = pawn(starting_space = player_2_starting_position)
det_die = deterministic_die()

while(True):
    pawn_1.take_turn(det_die)
    # pdb.set_trace()
    if (pawn_1.has_won()):
        print('Player 1 has won')
        print('Score of player 1:', pawn_1.score)
        print('Score of player 2:', pawn_2.score)
        print('Times die was rolled:', det_die.n_rolled)
        print('Puzzle solution:', pawn_2.score * det_die.n_rolled)
        break

    pawn_2.take_turn(det_die)
    # pdb.set_trace()
    if (pawn_2.has_won()):
        print('Player 2 has won')
        print('Score of player 2:', pawn_2.score)
        print('Score of player 1:', pawn_1.score)
        print('Times die was rolled:', det_die.n_rolled)
        print('Puzzle solution:', pawn_1.score * det_die.n_rolled)
        break
