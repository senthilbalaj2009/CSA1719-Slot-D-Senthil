from itertools import permutations

word1 = input("Enter first word: ").upper()
word2 = input("Enter second word: ").upper()
result = input("Enter result word: ").upper()

letters = set(word1 + word2 + result)
if len(letters) > 10:
    print("No solution possible: more than 10 letters")
else:
    found = False
    for p in permutations(range(10), len(letters)):
        d = dict(zip(letters, p))

        if any(d[w[0]] == 0 for w in (word1, word2, result)):
            continue

        n1 = int("".join(str(d[c]) for c in word1))
        n2 = int("".join(str(d[c]) for c in word2))
        n3 = int("".join(str(d[c]) for c in result))

        if n1 + n2 == n3:
            print("\nSolution found:")
            print(word1, "=", n1)
            print(word2, "=", n2)
            print(result, "=", n3)
            print("Letter mapping:", d)
            found = True
            break

    if not found:
        print("No solution exists")