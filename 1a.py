import sys

lines = [int(line.rstrip()) for line in sys.stdin]

for i, a in enumerate(lines):
    for b in lines[i+1:]:
        if a + b == 2020:
            print(f'{a} * {b} = {a*b}')
            exit(0)
