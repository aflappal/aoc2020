import sys

lines = [int(line.rstrip()) for line in sys.stdin]

for i, a in enumerate(lines):
    for j, b in enumerate(lines[i+1:]):
        for c in lines[j+1:]:
            if a + b + c == 2020:
                print(f'{a} * {b} * {c} = {a*b*c}')
                exit(0)
