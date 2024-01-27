try:
    with open("Custom_files/numbers.txt") as file:
        result = 0
        for line in file.readlines():
            current_num = int(line)
            result += current_num
        print(result)
except FileNotFoundError:
    print("File was not found")