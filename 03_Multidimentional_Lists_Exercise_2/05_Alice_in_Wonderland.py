def is_valid_move(matrix, row, col, n):
    return 0 <= row < n and 0 <= col < n and matrix[row][col] != 'R'


def alice_moves(matrix, start_row, start_col, n):
    alice_row, alice_col = start_row, start_col
    tea_collected = 0

    while True:
        command = input()

        if command == "up":
            new_row, new_col = alice_row - 1, alice_col
        elif command == "down":
            new_row, new_col = alice_row + 1, alice_col
        elif command == "left":
            new_row, new_col = alice_row, alice_col - 1
        elif command == "right":
            new_row, new_col = alice_row, alice_col + 1
        else:
            break  # Invalid command

        if not is_valid_move(matrix, new_row, new_col, n):
            break

        current_cell = matrix[new_row][new_col]
        if current_cell.isdigit():
            tea_collected += int(current_cell)
            if tea_collected >= 10:
                matrix[alice_row][alice_col] = '*'
                return True

        matrix[alice_row][alice_col] = '*'
        alice_row, alice_col = new_row, new_col

    return False



def print_matrix(matrix):
    for row in matrix:
        print(" ".join(row))


def main():
    n = int(input())
    matrix = [input().split() for _ in range(n)]

    # Find Alice and Rabbit Hole positions
    alice_row, alice_col = [(i, row.index('A')) for i, row in enumerate(matrix) if 'A' in row][0]
    rabbit_row, rabbit_col = [(i, row.index('R')) for i, row in enumerate(matrix) if 'R' in row][0]

    matrix[alice_row][alice_col] = '.'

    if alice_moves(matrix, alice_row, alice_col, n):
        print("She did it! She went to the party.")
    else:
        print("Alice didn't make it to the tea party.")

    print_matrix(matrix)


if __name__ == "__main__":
    main()
