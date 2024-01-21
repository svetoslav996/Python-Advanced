from collections import deque

materials = [int(x) for x in input().split()]
magic_level = deque(int(x) for x in input().split())

pattern = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle',
}

counters = {}

while True:
    if not materials or not magic_level:
        break
    material = materials.pop()
    m_lvl = magic_level.popleft()
    total_magic_lvl = material * m_lvl

    if total_magic_lvl in pattern.keys():
        if pattern[total_magic_lvl] not in counters.keys():
            counters[pattern[total_magic_lvl]] = 1
            continue
        counters[pattern[total_magic_lvl]] += 1
        continue

    if total_magic_lvl < 0:
        materials.append(material + m_lvl)

    elif total_magic_lvl > 0:
        material += 15
        materials.append(material)

    elif total_magic_lvl == 0:
        if material != 0:
            materials.append(material)
        if m_lvl != 0:
            magic_level.appendleft(m_lvl)

if 'Doll' in counters.keys() and 'Wooden train' in counters.keys() or \
        'Teddy bear' in counters.keys() and 'Bicycle' in counters.keys():
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials:
    materials = materials[::-1]
    print(f"Materials left: {', '.join(str(x) for x in materials)}")
if magic_level:
    print(f"Magic left: {', '.join(str(x) for x in magic_level)}")

for key, value in sorted(counters.items(), key=lambda x: x[0]):
    print(f"{key}: {value}")