sublists = input().split('|')

result = []
while sublists:
    sublist = sublists.pop().split()
    for el in sublist:
        result.append(el)

print(*result, sep=' ')