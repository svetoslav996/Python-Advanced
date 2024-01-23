from collections import deque
row, col = [int(el) for el in input().split()]
text = list(input())
snake = deque(text)
matrix = []
row_sample = []

num_el_in_matrix = row*col
for i in range(1, num_el_in_matrix + 1):
    char = snake.popleft()
    snake.append(char)
    row_sample.append(char)
    if i % col == 0:
        matrix.append(row_sample)
        row_sample = []

[
    print(*matrix[i][::-1], sep="") if i % 2 != 0
    else print(*matrix[i], sep="")
    for i in range(len(matrix))
]