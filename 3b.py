from functools import reduce
import operator
import sys

with open('3-input.txt') as f:
    lines = [line.rstrip() for line in f]

def trees_for_slope(dx, dy):
    w = len(lines[0])
    x = dx
    trees = 0
    for y in range(dy, len(lines), dy):
        if lines[y][x] == '#':
            trees += 1
        x = (x + dx) % w
    return trees

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
print(reduce(operator.mul, (trees_for_slope(*slope) for slope in slopes)))
