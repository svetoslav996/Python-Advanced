# TODO define winning conditions

class InvalidColumnError(Exception):
    pass


class FullColumnError(Exception):
    pass


# print matrix
def print_matrix(ma):
    for el in matrix:
        print(el)


def validate_column_choice(selected_column_num, max_column_index):
    # verify player choice of column number of is correct
    if not (0 <= selected_column_num <= max_column_index):
        raise InvalidColumnError


def place_player_choice(ma, selected_column_index, player_num):
    # Place player marker on the spot.
    # Check if the column is full if so - throw error.
    rows_count = len(ma)
    for row_index in range(rows_count - 1, -1, -1):
        current_element = ma[row_index][selected_column_index]
        if current_element == 0:
            ma[row_index][selected_column_index] = player_num
            return row_index, selected_column_index
    raise FullColumnError


def check_spot(row, col):
    if col < 0:
        return False


def is_player_num(ma, row, col, player_num):
    if col < 0 or row < 0:
        return False
    try:
        if ma[row][col] == player_num:
            return True
    except IndexError:
        return False
    return False


def is_winner(ma, row, col, player_num, slots_count=4):
    is_right = all([is_player_num(ma, row, col+index, player_num) for index in range(slots_count)])
    is_left = all([is_player_num(ma, row, col-index, player_num) for index in range(slots_count)])
    is_up = all([is_player_num(ma, row - index, col, player_num) for index in range(slots_count)])
    is_down = all([is_player_num(ma, row + index, col, player_num) for index in range(slots_count)])
    is_right_up = all([is_player_num(ma, row - index, col + index, player_num) for index in range(slots_count)])
    is_left_up = all([is_player_num(ma, row - index, col - index, player_num) for index in range(slots_count)])
    is_right_down = all([is_player_num(ma, row + index, col + index, player_num) for index in range(slots_count)])
    is_left_down = all([is_player_num(ma, row + index, col - index, player_num) for index in range(slots_count)])

    if any([is_right, is_left, is_down, is_up, is_right_up, is_left_up, is_right_down, is_left_down]):
        return True
    return False


rows_count = 6
cols_count = 7

# create matrix
matrix = [[0 for _ in range(cols_count)] for row_num in range(rows_count)]
print_matrix(matrix)

player_num = 1
while True:
    player_num = 2 if player_num % 2 == 0 else 1
    try:
        # Read column choice from input
        colum_num = int(input(f"Player {player_num}, please choose a comlumn: ")) - 1
        validate_column_choice(colum_num, cols_count - 1)
        row, col = place_player_choice(matrix, colum_num, player_num)
        if is_winner(matrix, row, col, player_num):
            print_matrix(matrix)
            print(f"The winner is player {player_num}")
            break
        print_matrix(matrix)
    except InvalidColumnError:
        print(f"This column is not valid. Please select a "
              f"number between {1} and {cols_count}")
        continue
    except ValueError:
        print(f"Please select a valid digit!")
        continue
    except FullColumnError:
        print(f"This column is already full! Please, select other column number!")
        continue
    player_num += 1
