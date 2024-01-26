def sum_numbers(num1, num2):
    return num1 + num2


def subtract_numbers(num1, num2, num3):
    return num1 - num2 - num3


def multiply_numbers(num1, num2):
    return num1 * num2


def func_executor(*args):
    result = []
    for func_ref, func_params in args:
        func_result = func_ref(*func_params)
        result.append(func_result)
    return result


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4)), (subtract_numbers, (30, 20, 10))))
