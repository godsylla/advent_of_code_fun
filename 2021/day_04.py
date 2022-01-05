"""
Day 4 Part 1 Directions: https://adventofcode.com/2021/day/4
"""
from icecream import ic 
import numpy as np

# Part 1 
def winner_or_not(shadow_board: np.array):
    """Checks if the board is a winning board or not.
    Winner if there is a row or column of selected numbers.
    :shadow_board: boolean board with marked numbers
        a board is 5 x 5 
        numbers are strings
    """
    column_check = [shadow_board[:, i].sum() for i in range(5)]
    row_check = [shadow_board[i, :].sum() for i in range(5)]
    return any(r == 5 for r in row_check) or any(c == 5 for c in column_check)
    

def mark_called_number(called_num: int, board: np.array, shadow_board: np.array):
    shadow_board += board == called_num
    return shadow_board


def find_winning_board(numbers, boards, shadow_boards):
    winning_board = None
    winning_shadow = None
    last_num_called = None

    while winning_board is None:
        for num in numbers:
            for i, (b, sb) in enumerate(zip(boards, shadow_boards)):
                shadow_boards[i] = mark_called_number(num, b, sb)
            
                if winner_or_not(shadow_boards[i]):
                    winning_board = boards[i]
                    winning_shadow = shadow_boards[i]

            if winning_board is not None:
                last_num_called = num
                break

    return winning_board, winning_shadow, last_num_called


if __name__ == '__main__':

    # Read and Parse Input ==========================================
    with open('./04-12-2021_input.txt', 'r') as f:
        parsed_lines = f.readlines()

    bingo_drawn_numbers = [int(n) for n in parsed_lines[0].split(',')]
    
    # Separate out each of the bingo boards
    boards = list()
    board = list()
    for b in parsed_lines[1:]:
        if len(b) > 1:
            numbers = b.split(' ')
            numbers = [int(n) for n in numbers if n != '']
            board.append(numbers)
        else:
            boards.append(np.array(board))
            board = list()
            
    boards = np.array(boards[1:])
    marked = np.zeros_like(boards, dtype=bool)

    
    # Part 1 =========================================================
    print('\nPart1')
    win_board, win_marked, win_num = find_winning_board(bingo_drawn_numbers, boards, marked)
    ic(win_board)
    ic(win_marked)
    ic(win_num)

    sum_unmarked = (win_board[win_marked == False]).sum()
    ic(sum_unmarked * win_num)
