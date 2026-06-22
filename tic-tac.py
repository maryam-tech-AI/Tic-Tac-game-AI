"""
Tic-Tac-Toe Minimax AI
Course: Artificial Intelligence

This program is a fully working Human vs AI Tic-Tac-Toe game.
Human plays as O.
AI plays as X and uses Minimax with depth-based scoring.

Scoring:
X wins = 10 - depth
O wins = depth - 10
Draw   = 0
"""

HUMAN = "O"
AI = "X"
EMPTY = " "


def print_board(board):
    """Display the Tic-Tac-Toe board."""
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def print_cell_numbers():
    """Show cell numbers to guide the player."""
    print("Cell numbers:")
    print()
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")
    print()


def available_moves(board):
    """Return list of empty cell indexes."""
    return [i for i in range(9) if board[i] == EMPTY]


def check_winner(board):
    """Return X if AI wins, O if Human wins, Draw if draw, otherwise None."""
    win_patterns = [
        (0, 1, 2),  # first row
        (3, 4, 5),  # second row
        (6, 7, 8),  # third row
        (0, 3, 6),  # first column
        (1, 4, 7),  # second column
        (2, 5, 8),  # third column
        (0, 4, 8),  # diagonal
        (2, 4, 6),  # diagonal
    ]

    for a, b, c in win_patterns:
        if board[a] == board[b] == board[c] and board[a] != EMPTY:
            return board[a]

    if EMPTY not in board:
        return "Draw"

    return None


def minimax(board, depth, is_maximizing):
    """
    Recursive Minimax algorithm.

    AI is Maximizer, so AI tries to get maximum score.
    Human is Minimizer, so Human tries to get minimum score.
    """
    result = check_winner(board)

    if result == AI:
        return 10 - depth

    if result == HUMAN:
        return depth - 10

    if result == "Draw":
        return 0

    if is_maximizing:
        best_score = -1000

        for move in available_moves(board):
            board[move] = AI
            score = minimax(board, depth + 1, False)
            board[move] = EMPTY

            if score > best_score:
                best_score = score

        return best_score

    else:
        best_score = 1000

        for move in available_moves(board):
            board[move] = HUMAN
            score = minimax(board, depth + 1, True)
            board[move] = EMPTY

            if score < best_score:
                best_score = score

        return best_score


def get_best_move(board):
    """
    Return the best move index for AI.
    This is the main function required in the assignment.
    """
    best_score = -1000
    best_move = None

    for move in available_moves(board):
        board[move] = AI
        score = minimax(board, 0, False)
        board[move] = EMPTY

        if score > best_score:
            best_score = score
            best_move = move

    return best_move


def human_turn(board):
    """Take valid input from human player."""
    while True:
        try:
            choice = int(input("Enter your move (1-9): "))
            index = choice - 1

            if choice < 1 or choice > 9:
                print("Invalid input. Please enter number from 1 to 9.")
                continue

            if board[index] != EMPTY:
                print("This cell is already filled. Choose another cell.")
                continue

            board[index] = HUMAN
            break

        except ValueError:
            print("Invalid input. Please enter a number only.")


def ai_turn(board):
    """AI chooses best move using Minimax."""
    move = get_best_move(board)

    if move is not None:
        board[move] = AI
        print(f"AI selected cell: {move + 1}")


def play_game():
    """Main game loop."""
    board = [EMPTY] * 9

    print("=" * 40)
    print("Tic-Tac-Toe Minimax AI")
    print("=" * 40)
    print("Human = O")
    print("AI    = X")
    print()
    print_cell_numbers()

    while True:
        print_board(board)

        human_turn(board)

        result = check_winner(board)
        if result is not None:
            print_board(board)
            show_result(result)
            break

        ai_turn(board)

        result = check_winner(board)
        if result is not None:
            print_board(board)
            show_result(result)
            break


def show_result(result):
    """Display final result."""
    if result == AI:
        print("AI wins!")
    elif result == HUMAN:
        print("Human wins!")
    else:
        print("Game draw!")


def main():
    """Program entry point."""
    while True:
        play_game()

        again = input("\nDo you want to play again? (y/n): ").lower().strip()

        if again != "y":
            print("Thank you for playing.")
            input("Press Enter to exit...")
            break


if __name__ == "__main__":
    main()
