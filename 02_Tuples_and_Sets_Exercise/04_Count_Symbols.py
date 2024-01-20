line = input()
chars_counts = {}

for ch in line:
    if ch in chars_counts:
        chars_counts[ch] += 1
    else:
        chars_counts[ch] = 1

for key, value in sorted(chars_counts.items()):
    print(f"{key}: {value} time/s")