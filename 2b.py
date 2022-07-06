import sys

def isvalid(idx1, idx2, char, password):
    idx1 -= 1
    idx2 -= 1
    return char in (password[idx1], password[idx2]) and password[idx1] != password[idx2]

def parse(line):
    parts = line.split()
    pos1, pos2 = list(map(int, parts[0].split('-')))
    char = parts[1].rstrip(':')
    password = parts[2]
    return pos1, pos2, char, password

with open('2-input.txt') as f:
    lines = [line.rstrip() for line in f]
print(sum(isvalid(*parse(line)) for line in lines))
