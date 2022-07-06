import sys

def isvalid(at_least, at_most, char, password):
    return at_least <= password.count(char) <= at_most

def parse(line):
    parts = line.split()
    at_least, at_most = list(map(int, parts[0].split('-')))
    char = parts[1].rstrip(':')
    password = parts[2]
    return at_least, at_most, char, password

with open('2-input.txt') as f:
    lines = [line.rstrip() for line in f]
print(sum(isvalid(*parse(line)) for line in lines))
