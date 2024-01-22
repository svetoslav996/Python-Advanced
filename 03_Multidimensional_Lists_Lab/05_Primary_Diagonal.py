def primary_diagonal_sum(matrix):
    size = len(matrix)
    diagonal_sum = sum(matrix[i][i] for i in range(size))
    return diagonal_sum

def read_matrix():
    size = int(input())
    matrix = []

    for _ in range(size):
        row = list(map(int, input().split()))
        matrix.append(row)

    return matrix

if __name__ == "__main__":
    # Read matrix from the console
    matrix = read_matrix()

    # Calculate and print the sum of the primary diagonal
    diagonal_sum = primary_diagonal_sum(matrix)
    print(diagonal_sum)
