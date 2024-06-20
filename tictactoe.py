import math

WIN = 1000
DRAW = 0
LOSS = -1000

AI_MARKER = 'O'
PLAYER_MARKER = 'X'
EMPTY_SPACE = '-'

START_DEPTH = 0


def print_game_state(state):
    if WIN == state:
        print("WIN")
    elif DRAW == state:
        print("DRAW")
    elif LOSS == state:
        print("LOSS")


# all possible winning states
winning_states = [
    # row
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],

    # column
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],

    # diagonal
    [(0, 0), (1, 1), (2, 2)],
    [(2, 0), (1, 1), (0, 2)]
]

# current board state


def print_board(board):
    for i in range(3):
        for j in range(3):
            print(board[i][j], end=" ")
            if j < 2:
                print("|", end=" ")
        print()
        if i < 2:
            print("---------")
    print()

# available legal moves


def get_legal_moves(board):
    legal_moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY_SPACE:
                legal_moves.append((i, j))
    return legal_moves

# to check if position is occupied


def position_occupied(board, pos):
    return board[pos[0]][pos[1]] != EMPTY_SPACE

# all board positions occupied by the given marker


def get_occupied_positions(board, marker):
    occupied_positions = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == marker:
                occupied_positions.append((i, j))
    return occupied_positions

# to check if the board is full


def board_is_full(board):
    return not any(EMPTY_SPACE in row for row in board)

# to check if the game has been won


def game_is_won(occupied_positions):
    for win_state in winning_states:
        if all(pos in occupied_positions for pos in win_state):
            return True
    return False


def get_opponent_marker(marker):
    return PLAYER_MARKER if marker == AI_MARKER else AI_MARKER

# to check if someone has won or lost


def get_board_state(board, marker):
    opponent_marker = get_opponent_marker(marker)

    if game_is_won(get_occupied_positions(board, marker)):
        return WIN

    if game_is_won(get_occupied_positions(board, opponent_marker)):
        return LOSS

    if board_is_full(board):
        return DRAW

    return DRAW

# minimax algo


def minimax_optimization(board, marker, depth, alpha, beta):
    best_move = (-1, -1)
    best_score = LOSS if marker == AI_MARKER else WIN

    if board_is_full(board) or get_board_state(board, AI_MARKER) != DRAW:
        return get_board_state(board, AI_MARKER), best_move

    for move in get_legal_moves(board):
        board[move[0]][move[1]] = marker
        score, _ = minimax_optimization(
            board, get_opponent_marker(marker), depth + 1, alpha, beta)
        board[move[0]][move[1]] = EMPTY_SPACE      # Undo move

        if marker == AI_MARKER:
            if score > best_score:
                best_score = score - depth * 10
                best_move = move
                alpha = max(alpha, best_score)
        else:
            if score < best_score:
                best_score = score + depth * 10
                best_move = move
                beta = min(beta, best_score)

        if beta <= alpha:
            break

    return best_score, best_move

# to check if the game is finished


def game_is_done(board):
    return board_is_full(board) or get_board_state(board, AI_MARKER) != DRAW


def main():
    board = [[EMPTY_SPACE, EMPTY_SPACE, EMPTY_SPACE],
             [EMPTY_SPACE, EMPTY_SPACE, EMPTY_SPACE],
             [EMPTY_SPACE, EMPTY_SPACE, EMPTY_SPACE]]

    print("********************************\n\n\tTic Tac Toe AI\n\n********************************")
    print("Player = X\t AI Computer = O\n")

    print_board(board)

    while not game_is_done(board):
        try:
            row, col = map(int, input(
                "Enter your move (row and column): ").split())
            row -= 1
            col -= 1
        except ValueError:
            print("Invalid input. Please enter two numbers separated by a space.")
            continue

        if row < 0 or row >= 3 or col < 0 or col >= 3:
            print("Invalid move. Row and column must be between 1 and 3.")
            continue

        if position_occupied(board, (row, col)):
            print("The position ({}, {}) is occupied. Try another one...".format(
                row + 1, col + 1))
            continue

        board[row][col] = PLAYER_MARKER
        print_board(board)

        if game_is_done(board):
            break

        _, ai_move = minimax_optimization(
            board, AI_MARKER, START_DEPTH, LOSS, WIN)
        if ai_move != (-1, -1):
            board[ai_move[0]][ai_move[1]] = AI_MARKER

        print_board(board)

    print("********** GAME OVER **********\n")
    player_state = get_board_state(board, PLAYER_MARKER)
    print("PLAYER ", end="")
    print_game_state(player_state)


if __name__ == "__main__":
    main()
