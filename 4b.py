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
    def validate_byr(value):
        year = int(value)
        return 1920 <= year <= 2002

    def validate_iyr(value):
        year = int(value)
        return 2010 <= year <= 2020

    def validate_eyr(value):
        year = int(value)
        return 2020 <= year <= 2030

    def validate_hgt(value):
        if value.endswith('cm'):
            height = int(value[:-2])
            return 150 <= height <= 193
        elif value.endswith('in'):
            height = int(value[:-2])
            return 59 <= height <= 76
        else:
            return False

    def validate_hcl(value):
        if value[0] != '#':
            return False
        if len(value[1:]) != 6:
            return False
        # make sure the value is hexadecimal
        try:
            int(value[1:], 16)
        except ValueError:
            return False
        return True

    def validate_ecl(value):
        return value in ('amb', 'blu', 'brn', 'grn', 'gry', 'hzl', 'oth')

    def validate_pid(value):
        if len(value) != 9:
            return False
        try:
            int(value)
        except ValueError:
            return False
        return True

    validate_funcs = {
            'byr': validate_byr,
            'iyr': validate_iyr,
            'eyr': validate_eyr,
            'hgt': validate_hgt,
            'hcl': validate_hcl,
            'ecl': validate_ecl,
            'pid': validate_pid
            }
    fvs = get_fvs(line)
    fields = [fv[0] for fv in fvs]
    return (all(req in fields for req in validate_funcs)
            and all(validate_funcs[fv[0]](fv[1]) for fv in fvs if fv[0] != 'cid'))

lines = []
curr = []
for line in raw_lines:
    if line != '':
        curr.append(line)
    else:
        lines.append(' '.join(curr))
        curr = []

print(sum(isvalid(line) for line in lines))
