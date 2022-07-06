import sys

with open('6-input.txt') as f:
    raw_lines = [line.rstrip() for line in f]

if raw_lines[-1] != '':
    raw_lines.append('')

def get_group(lines):
    group = []
    for line in lines:
        if line != '':
            group.append(line)
        else:
            yield group
            group = []

def num_yes_in_group(group):
    yeses = set(group[0])
    for answers in group[1:]:
        yeses &= set(answers)
    return len(yeses)

print(sum(num_yes_in_group(group) for group in get_group(raw_lines)))
