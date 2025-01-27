# def triangle( n:int) ->None:
#     for i in range(n+1):
#         for j in range(i):
#             print(i, end=" ")
#         print()
# triangle(6)


# 1      1
# 12    12
# 123  123
# 12341234
# n=4
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(j, end=' ')
#     for space in range(1, 4*(n-i)+1):
#         print(end=' ')
#     for j in range(i, 0, -1):
#         print(j, end=' ')
#     print()
    
# rows = 3  # Number of rows

# for i in range(1, rows + 1):
#     # First half: numbers in ascending order
#     for j in range(1, i + 1):
#         print(j, end=" ")

#     # Spaces in the middle
#     spaces = (rows - i) * 2  # Calculate spaces based on current row
#     print("  " * spaces, end="")

#     # Second half: numbers in descending order
#     for j in range(i, 0, -1):
#         print(j, end=" ")

#     print()  # Move to the next line
# 1         1
# 1 2     2 1
# 1 2 3 3 2 1
def hollowDiamond(n: int):
    for row in range(1, n + 1):
        for col in range(1, n * 2):
            # Top half: stars and spaces
            if row == 1 or row == n:
                print("*", end=" ")  # Full row of stars for the first and last rows
            else:
                if col <= n - row + 1 or col >= n + row - 1:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
        print()  # Move to the next line

# Call the function with n = 3
hollowDiamond(8)
