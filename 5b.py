import sys


with open('5-input.txt') as f:
    lines = [line.rstrip() for line in f]


def binsearch(highest, input_, low_char, high_char):
    low = 0
    high = highest
    for side in input_:
        assert side in (low_char, high_char)
        if side == low_char:
            high = (high + low) // 2
        else:
            low = (high + low) // 2 + 1
    assert low == high, (low, high)
    return low


def id_for_line(line):
    row = binsearch(127, line[:7], 'F', 'B')
    col = binsearch(7, line[7:], 'L', 'R')
    return row * 8 + col


def find_my_id(ids):
    sorted_ids = sorted(ids)
    for i in range(1, len(sorted_ids)):
        if sorted_ids[i] - 1 != sorted_ids[i-1]:
            return sorted_ids[i] - 1
    return -1


print(find_my_id(id_for_line(line) for line in lines))
