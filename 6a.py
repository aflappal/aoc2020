import sys

with open('6-input.txt') as f:
    raw_lines = [line.rstrip() for line in f]

if raw_lines[-1] != '':
    raw_lines.append('')

lines = []
curr = []
for line in raw_lines:
    if line != '':
        curr.append(line)
    else:
        lines.append(''.join(curr))
        curr = []

print(sum(len(set(line)) for line in lines))
