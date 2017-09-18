from random import randint

board = []

for item in range(5):
    board.append(['O'] * 5)

def print_board(board_in):
    for row in board_in:
        print ' '.join(row)

print 'Let\'s play Battleship!'
print ''
print 'Board:'
print_board(board)

def random_row(board_in):
    return randint(0, len(board_in) - 1)
def random_col(board_in):
    return randint(0, len(board_in) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

for turn in range(4):
    print ''
    print 'Turn', turn + 1
    print ''

    guess_row = int(raw_input('Guess Row: '))
    guess_col = int (raw_input('Guess Col: '))

    if(guess_row == ship_row and guess_col == ship_col):
        print ''
        print 'Congratulations! You sank my Battleship!'
        break
    else:
        if(not guess_row in range(5) or not guess_col in range(5)):
            print ''
            print 'Oops, that\'s not even in the ocean.'
        elif(board[guess_row][guess_col] == 'X'):
            print ''
            print 'You guessed that already.'
        else:
            print ''
            print 'You missed my Battleship.'
            print ''
            board[guess_row][guess_col] = 'X'
            print_board(board)
        if(turn == 3):
            print ''
            print 'Game Over.'