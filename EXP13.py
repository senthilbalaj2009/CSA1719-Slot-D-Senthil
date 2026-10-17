
def minimax(board, is_max):
    if "X" in board and board.count("X") == 3:
        pass

    wins = [(0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6)]

    for a, b, c in wins:
        if board[a] == board[b] == board[c] == "X":
            return 1
        if board[a] == board[b] == board[c] == "O":
            return -1

    if " " not in board:
        return 0

    if is_max:
        best = -float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                best = max(best, minimax(board, False))
                board[i] = " "
        return best
    else:
        best = float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                best = min(best, minimax(board, True))
                board[i] = " "
        return best

board = input("Enter board (9 characters, use - for empty): ")
board = [" " if x == "-" else x.upper() for x in board]

best_score = -float("inf")
best_move = -1

for i in range(9):
    if board[i] == " ":
        board[i] = "X"
        score = minimax(board, False)
        board[i] = " "

        if score > best_score:
            best_score = score
            best_move = i

if best_move != -1:
    board[best_move] = "X"

print("Best move for X:", best_move + 1)
for i in range(0, 9, 3):
    print(" | ".join(board[i:i+3]))
