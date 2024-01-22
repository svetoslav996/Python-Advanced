def filter_even_numbers(matrix):
    even_matrix = [[num for num in row if num % 2 == 0] for row in matrix]
    return even_matrix

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

    # Filter even numbers and print the resulting matrix
    even_matrix = filter_even_numbers(matrix)
    print(even_matrix)
