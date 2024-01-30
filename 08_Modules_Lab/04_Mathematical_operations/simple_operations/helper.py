from operation_functions import sum_nums, sub_nums, div_nums, mul_nums, pow_nums

operation_mapper = {
    "+": lambda a, b: a + b,
    "-": sub_nums,
    "*": mul_nums,
    "/": div_nums,
    "^": pow_nums
}


def calculate(sign, a, b):
    if sign in ("+", "-", "/", "*"):
        return eval(f"{a} {sign} {b}")
    if sign == "^":
        return a ** b
    else:
        raise ValueError("Sign is not defined")
