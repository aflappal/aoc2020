import sys

with open('3-input.txt') as f:
    lines = [line.rstrip() for line in f]

w = len(lines[0])
x = 3
trees = 0
for line in lines[1:]:
    if line[x] == '#':
        trees += 1
    x = (x + 3) % w
print(trees)
