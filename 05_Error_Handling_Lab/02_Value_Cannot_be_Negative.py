class ValueCannotBeNegative(Exception):
    pass

def read_numbers():
    numbers = []
    for _ in range(5):
        num = int(input())
        if num < 0:
            raise ValueCannotBeNegative
        numbers.append(num)
    return numbers

try:
    print()
    result = read_numbers()
    print(result)
except ValueCannotBeNegative:
    print("Traceback (most recent call last):")
    print("  File \"value_cannot_be_negative.py\", line 8, in <module>")
    print("    raise ValueCannotBeNegative")
    print("__main__.ValueCannotBeNegative")
