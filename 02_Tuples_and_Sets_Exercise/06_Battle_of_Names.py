n = int(input())

odd = set()
even = set()

even_sum = 0
odd_sum = 0

for row in range(1, n + 1):
    name_sum = sum([ord(x) for x in input()]) // row
    if name_sum % 2 == 0:
        even.add(name_sum)
        even_sum += name_sum
    else:
        odd.add(name_sum)
        odd_sum += name_sum

if even_sum == odd_sum:
    result = odd.union(even)
elif even_sum > odd_sum:
    result = odd.symmetric_difference(even)
else:
    result = odd.difference(even)

print(*result, sep=', ')