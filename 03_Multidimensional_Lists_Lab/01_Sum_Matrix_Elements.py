def read_matrix():
    rows, columns = map(int, input().split(', '))
    matrix = []

    for _ in range(rows):
        row = list(map(int, input().split(', ')))
        matrix.append(row)

    return matrix

def print_matrix_sum(matrix):
    total_sum = sum(sum(row) for row in matrix)
    print(total_sum)

def print_matrix(matrix):
    print(matrix)

if __name__ == "__main__":
    # Read matrix from the console
    matrix = read_matrix()

    # Print the sum of all numbers in the matrix
    print_matrix_sum(matrix)

    # Print the matrix itself
    print_matrix(matrix)
