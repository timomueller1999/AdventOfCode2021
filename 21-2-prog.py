board_size = 10
winning_score = 21

n_1_wins_matrix = np.zeros((board_size,board_size,30,2))
n_2_wins_matrix = np.zeros((board_size,board_size,30,2))

def n_wins(
    pos_player_1: int,      # between 0 and 9;
    pos_player_2: int,      # 0 represents 10
    score_player_1: int,
    score_player_2: int,
    on_the_move: int,       # 0 or 1; if 1, then player 1 has the move;
                            # if 0, player 2 has the move
):

    if (on_the_move == 1)       # player 1 has the move
        n_1_wins = 0
        n_2_wins = 0
        for die_score, amount in [(3,1), (4,3), (5,6), (6,7), (7,6), (8,3), (9,1)]:
            temp_pos_player_1 = (pos_player_1 + die_score) % board_size
            if temp_pos_player_1 == 0:
                temp_score_player_1 = score_player_1 + 10
            else:
                temp_score_player_1 = score_player_1 + temp_pos_player_1

            n_1_wins += n_1_wins_matrix[
                temp_pos_player_1,
                pos_player_2,
                temp_score_player_1,
                score_player_2,
                0,
            ]

            n_2_wins += n_2_wins_matrix[
                temp_pos_player_1,
                pos_player_2,
                temp_score_player_1,
                score_player_2,
                0,
            ]

    elif (on_the_move == 0)     # player 2 has the move
        n_1_wins = 0
        n_2_wins = 0
        for die_score, amount in [(3,1), (4,3), (5,6), (6,7), (7,6), (8,3), (9,1)]:
            temp_pos_player_2 = (pos_player_2 + die_score) % board_size
            if temp_pos_player_2 == 0:
                temp_score_player_2 = score_player_2 + 10
            else:
                temp_score_player_2 = score_player_2 + temp_pos_player_2

            n_1_wins += n_1_wins_matrix[
                pos_player_1,
                temp_pos_player_2,
                score_player_1,
                temp_score_player_2,
                0,
            ]

            n_2_wins += n_2_wins_matrix[
                pos_player_1,
                temp_pos_player_2,
                score_player_1,
                temp_score_player_2,
                0,
            ]

    return n_1_wins, n_2_wins


## Initialize the n_1_wins_matrix and n_2_wins_matrix with senseful values when one player has already won:
