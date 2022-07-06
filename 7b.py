import sys

with open('7-input.txt') as f:
    lines = [line.rstrip() for line in f]

def parse_line(line):
    def get_contents(raw_contents):
        return list(map(lambda raw: (' '.join(raw.split()[1:3]), raw.split()[0]), raw_contents))

    sentences = line.split(', ')
    first_part = sentences[0].split(' bags contain ')
    container = first_part[0]
    contents_raw = sentences[1:]
    contents = []
    if not first_part[1].startswith('no'):
        contents_raw.append(first_part[1])
        contents = get_contents(contents_raw)
    return container, contents

contains = {}
for line in lines:
    container, contents = parse_line(line)
    for content in contents:
        contains[container] = contents

root = 'shiny gold'
memo = {}

def count_contents(container, level=0):
    indent = ' ' * level
    print(f'{indent}container: {container}')
    if container in memo:
        print(f'{indent}seen before, has {memo[container]} contents')
        return memo[container]
    children = 0
    for content, num_ in contains.get(container, []):
        num = int(num_)
        children += num + num * count_contents(content, level+1)
    print(f'{indent}container {container} has {children} immediate contents')
    memo[container] = children
    return children

print(count_contents(root))
