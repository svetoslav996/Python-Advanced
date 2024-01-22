def flatten_matrix(matrix):
    flattened_list = [num for row in matrix for num in row]
    return flattened_list

def read_matrix():
    rows = int(input())
    matrix = []

    for _ in range(rows):
        row = list(map(int, input().split(', ')))
        matrix.append(row)

    return matrix

if __name__ == "__main__":
    # Read matrix from the console
    matrix = read_matrix()

    # Flatten the matrix and print the resulting list
    flattened_list = flatten_matrix(matrix)
    print(flattened_list)
