from simple_operations.helper import operation_mapper, calculate

data = input().split()

a = float(data[0])
sign = data[1]
b = float(data[2])

try:
    print(calculate(sign, a, b))
except ZeroDivisionError:
    print("Invalid number b. Should not be 0 if divide")
