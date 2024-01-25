def operate(sign, *args):
    if sign == "+":
        result = 0
        for el in args:
            result += el
    elif sign == "-":
        result = args[0] if len(args) > 0 else 0
        for el in args[1:]:
            result -= el
    elif sign == "*":
        result = 1
        for el in args:
            result *= el
    elif sign == "/":
        if len(args) == 0:
            raise ValueError("Division requires at least one argument")
        result = args[0]
        for el in args[1:]:
            if el == 0:
                raise ValueError("Cannot divide by zero")
            result /= el
    else:
        raise ValueError("Invalid operator. Supported operators are '+', '-', '*', '/'.")

    return result

# Examples
print(operate("+", 1, 2, 3))  # Output: 6
print(operate("*", 3, 4))
