def move_santa(direction):
    global SantaRow, SantaCol, ranOutOfPresents, kidsWithPresents, countOfPresents, niceKids

    row, col = SantaRow, SantaCol

    if direction == "up":
        row -= 1
    elif direction == "down":
        row += 1
    elif direction == "left":
        col -= 1
    elif direction == "right":
        col += 1

    in_bounds = check_if_in_bounds(row, col)

    if in_bounds:
        current_cell = neighborhood[row][col]

        if current_cell == 'V':
            kidsWithPresents += 1
            niceKids -= 1
            countOfPresents -= 1

            if countOfPresents <= 0:
                ranOutOfPresents = True
        elif current_cell == 'C':
            give_presents(row, col)

    SantaRow, SantaCol = row, col
    neighborhood[SantaRow][SantaCol] = 'S'


def give_presents(row, col):
    global ranOutOfPresents, kidsWithPresents, countOfPresents, niceKids

    up = neighborhood[row - 1][col]
    down = neighborhood[row + 1][col]
    left = neighborhood[row][col - 1]
    right = neighborhood[row][col + 1]

    cells = [up, down, left, right]

    for cell in cells:
        if cell == 'V' or cell == 'X':
            if cell == 'V':
                niceKids -= 1

            kidsWithPresents += 1
            countOfPresents -= 1

            if countOfPresents <= 0:
                ranOutOfPresents = True
                break

    neighborhood[row - 1][col] = '-'
    neighborhood[row + 1][col] = '-'
    neighborhood[row][col - 1] = '-'
    neighborhood[row][col + 1] = '-'


def check_if_in_bounds(row, col):
    return 0 <= row < len(neighborhood) and 0 <= col < len(neighborhood[row])


def read_neighborhood():
    global SantaRow, SantaCol, niceKids, countNiceKids

    for row in range(len(neighborhood)):
        elements = input().split()

        for col in range(len(elements)):
            current_char = elements[col][0]

            if current_char == 'S':
                SantaRow, SantaCol = row, col
            elif current_char == 'V':
                niceKids += 1
                countNiceKids += 1

            neighborhood[row][col] = current_char



def print_neighborhood():
    for row in neighborhood:
        print(" ".join(row))


if __name__ == "__main__":
    countOfPresents = int(input())
    size = int(input())

    neighborhood = [['' for _ in range(size)] for _ in range(size)]

    SantaRow, SantaCol = 0, 0
    countNiceKids = 0
    niceKids = 0
    kidsWithPresents = 0
    ranOutOfPresents = False

    read_neighborhood = input()

    direction = input().strip()
    while direction != "Christmas morning":
        neighborhood[SantaRow][SantaCol] = '-'
        move_santa(direction)

        if ranOutOfPresents:
            print("Santa ran out of presents!")
            break

        direction = input().strip()

    print_neighborhood()

    if niceKids == 0:
        print(f"Good job, Santa! {kidsWithPresents} happy nice kid/s.")
    else:
        print(f"No presents for {countNiceKids - kidsWithPresents} nice kid/s.")
