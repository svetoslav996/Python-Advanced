n = int(input())
elements = set()

for _ in range(n):
    current_elements = input().split()
    elements = elements.union(current_elements)

for element in elements:
    print(element)