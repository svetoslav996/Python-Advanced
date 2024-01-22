rows = int(input())

# Assuming a square matrix, so cols = rows
cols = rows

matrix = []

# Populate the matrix
for _ in range(rows):
    symbols = input()
    row = [char for char in symbols]
    matrix.append(row)

symbol = input()
is_found = False

for row in range(rows):
    for col in range(cols):
        if matrix[row][col] == symbol:
            print(f"({row}, {col})")
            is_found = True
            break

if not is_found:
    print(f"{symbol} does not occur in the matrix")
