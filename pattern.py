# def nStarTriangle(n: int) -> None:
#     stars = 1
#     empty = n-1
#     for i in range(n):
#         print("{}{}{}".format(' '*empty, '*'*stars, ' '*empty))
#         stars+=2
#         empty-=1
# nStarTriangle(3)

# def reverseStarTriangle(n: int) -> None:
#     stars = 2 * n - 1
#     empty = 0
#     for i in range(n):
#         print("{}{}{}".format(' ' * empty, '*' * stars, ' ' * empty))
#         stars -= 2
#         empty += 1

# reverseStarTriangle(3)
# Binary Number Triangle

rows = 5  # Number of rows for the pattern

for i in range(1, rows + 1):
    for j in range(i):
        print((j + i) % 2, end=" ")
    print()
