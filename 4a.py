import sys

with open('4-input.txt') as f:
    raw_lines = [line.rstrip() for line in f]

if raw_lines[-1] != '':
    raw_lines.append('')

def get_fvs(line):
    raw_fvs = line.split()
    fvs = [tuple(raw_fv.split(':')) for raw_fv in raw_fvs]
    return fvs

def isvalid(line):
    required = ['byr',
                'iyr',
                'eyr',
                'hgt',
                'hcl',
                'ecl',
                'pid']
    fvs = get_fvs(line)
    fields = [fv[0] for fv in fvs]
    return all(req in fields for req in required)

lines = []
curr = []
for line in raw_lines:
    if line != '':
        curr.append(line)
    else:
        lines.append(' '.join(curr))
        curr = []

print(sum(isvalid(line) for line in lines))
