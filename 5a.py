import sys

with open('5-input.txt') as f:
    lines = [line.rstrip() for line in f]

def binsearch(highest, inp, low_char, high_char):
    low = 0
    high = highest
    for c in inp:
        assert c in (low_char, high_char)
        if c == low_char:
            high = (high + low) // 2
        else:
            low = (high + low) // 2 + 1
    assert low == high, (low, high)
    return low


def id_for_line(line):
    row = binsearch(127, line[:7], 'F', 'B')
    col = binsearch(7, line[7:], 'L', 'R')
    return row * 8 + col

print(max(id_for_line(line) for line in lines))
