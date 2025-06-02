import math


board = [' ' for _ in range(9)]

def print_board():
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')


def winner(b, player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  
        [0,3,6], [1,4,7], [2,5,8],  
        [0,4,8], [2,4,6]            
    ]
    return any(all(b[i] == player for i in condition) for condition in win_conditions)


def is_draw():
    return ' ' not in board


def minimax(b, depth, is_maximizing):
    if winner(b, 'X'):
        return 1
    elif winner(b, 'O'):
        return -1
    elif is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'X'
                score = minimax(b, depth + 1, False)
                b[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'O'
                score = minimax(b, depth + 1, True)
                b[i] = ' '
                best_score = min(score, best_score)
        return best_score


def ai_move():
    best_score = -math.inf
    move = 0
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    board[move] = 'X'


def human_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] == ' ':
                board[move] = 'O'
                break
            else:
                print("That spot is taken.")
        except (IndexError, ValueError):
            print("Invalid move. Try a number between 1 and 9.")


def play():
    print("TIC-TAC-TOE\nYou are O, AI is X")
    print_board()

    while True:
        human_move()
        print_board()
        if winner(board, 'O'):
            print("You win!")
            break
        elif is_draw():
            print("It's a draw!")
            break

        print("AI's turn...")
        ai_move()
        print_board()
        if winner(board, 'X'):
            print("AI wins!")
            break
        elif is_draw():
            print("It's a draw!")
            break


play()
