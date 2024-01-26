command = input()
numbers = [int(x) for x in input().split()]

if command == 'Even':
    even_numbers = sum([x for x in numbers if x % 2 == 0]) * len(numbers)
    print(even_numbers)
else:
    odd_numbers = sum([x for x in numbers if x % 2 == 1]) * len(numbers)
    print(odd_numbers)