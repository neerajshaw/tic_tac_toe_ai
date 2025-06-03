import math

board = ['' for _ in range(9)]

def print_board():
    print()
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print(' | '.join([cell if cell != '' else ' ' for cell in row]))
        print('-' * 10)
    print()

def available_moves():
    return [i for i, spot in enumerate(board) if spot == '']

def make_move(position, player):
    if board[position] == '':
        board[position] = player
        return True
    return False

def winner(player):
    win_condition = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # cols
        [0,4,8], [2,4,6]            # diagonals
    ]
    for condition in win_condition:
        if all(board[i] == player for i in condition):
            return True
    return False

def is_draw():
    return '' not in board

def minimax(is_maximizing):
    if winner('O'):
        return 1
    if winner('X'):
        return -1
    if is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in available_moves():
            board[move] = 'O'
            score = minimax(False)
            board[move] = ''
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in available_moves():
            board[move] = 'X'
            score = minimax(True)
            board[move] = ''
            best_score = min(score, best_score)
        return best_score

def best_move():
    best_score = -math.inf
    move = None
    for i in available_moves():
        board[i] = 'O'
        score = minimax(False)
        board[i] = ''
        if score > best_score:
            best_score = score
            move = i
    return move

def main():
    print("Welcome to Tic Tac Toe!")
    print("You are 'X'. AI is 'O'. Board positions:")
    print("0 | 1 | 2")
    print("3 | 4 | 5")
    print("6 | 7 | 8")

    print_board()

    while True:
        try:
            user_move = int(input("Your move (0-8): "))
            if user_move not in available_moves():
                print("Invalid move. Try again.")
                continue
            make_move(user_move, 'X')
        except ValueError:
            print("Please enter a number between 0-8.")
            continue

        print_board()

        if winner("X"):
            print("You win!")
            break
        if is_draw():
            print("It's a draw.")
            break

        print("AI is thinking...")
        ai_move = best_move()
        make_move(ai_move, 'O')
        print_board()

        if winner('O'):
            print("AI wins!")
            break
        if is_draw():
            print("It's a draw.")
            break

if __name__ == "__main__":
    main()