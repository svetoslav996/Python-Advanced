def column_sums(matrix):
    num_columns = len(matrix[0])
    sums = [0] * num_columns

    for row in matrix:
        for j in range(num_columns):
            sums[j] += row[j]

    return sums

def read_matrix():
    rows, columns = map(int, input().split(', '))
    matrix = []

    for _ in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)

    return matrix

if __name__ == "__main__":
    # Read matrix from the console
    matrix = read_matrix()

    # Calculate and print the sum for each column
    sums = column_sums(matrix)
    for column_sum in sums:
        print(column_sum)
