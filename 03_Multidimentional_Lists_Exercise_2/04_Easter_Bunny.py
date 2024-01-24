n = int(input())
matrix, bunny_pos, best_positions = [], [], []
best_direction = ''
eggs_collected = float("-inf")
field_range = range(0, n)
paths = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for r in range(n):
    current_row = input().split()
    if "B" in current_row:
        bunny_pos.append(r)
        bunny_pos.append(current_row.index("B"))
    matrix.append(current_row)

for direction, coordinates in paths.items():
    matrix_copy = matrix.copy()
    bunny_pos_copy = bunny_pos.copy()
    current_positions = []
    eggs_current = 0

    while True:
        if bunny_pos_copy[0] + coordinates[0] in field_range \
                and bunny_pos_copy[1] + coordinates[1] in field_range \
                and matrix_copy[bunny_pos_copy[0] + coordinates[0]][bunny_pos_copy[1] + coordinates[1]] != "X":
            current_el = matrix_copy[bunny_pos_copy[0] + coordinates[0]][bunny_pos_copy[1] + coordinates[1]]
            eggs_current += int(current_el)
            bunny_pos_copy = [bunny_pos_copy[0] + coordinates[0], bunny_pos_copy[1] + coordinates[1]]
            current_positions.append(bunny_pos_copy)
        else:
            break

    if eggs_current > eggs_collected and current_positions:
        best_positions = current_positions
        eggs_collected = eggs_current
        best_direction = direction

print(best_direction)
[print(el) for el in best_positions]
print(eggs_collected)