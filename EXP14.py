
def minimax(coins, alpha, beta, maximizing):
    if coins == 0:
        return -1 if maximizing else 1

    if maximizing:
        best = -float("inf")
        for move in (1, 2):
            if coins >= move:
                score = minimax(coins - move, alpha, beta, False)
                best = max(best, score)
                alpha = max(alpha, best)
                if alpha >= beta:
                    break
        return best

    else:
        best = float("inf")
        for move in (1, 2):
            if coins >= move:
                score = minimax(coins - move, alpha, beta, True)
                best = min(best, score)
                beta = min(beta, best)
                if alpha >= beta:
                    break
        return best


coins = int(input("Enter number of coins: "))
turn = input("Who starts? (C = Computer, U = User): ").upper()

while coins > 0:
    print("\nCoins remaining:", coins)

    if turn == "C":
        best_score = -float("inf")
        best_move = 1

        for move in (1, 2):
            if coins >= move:
                score = minimax(
                    coins - move,
                    -float("inf"),
                    float("inf"),
                    False
                )
                if score > best_score:
                    best_score = score
                    best_move = move

        coins -= best_move
        print("Computer takes", best_move, "coin(s)")

        if coins == 0:
            print("Computer wins!")
            break

        turn = "U"

    else:
        try:
            move = int(input("Take 1 or 2 coins: "))
        except ValueError:
            print("Enter a valid number.")
            continue

        if move not in (1, 2) or move > coins:
            print("Invalid move! Try again.")
            continue

        coins -= move
        print("You take", move, "coin(s)")

        if coins == 0:
            print("You win!")
            break

        turn = "C"
