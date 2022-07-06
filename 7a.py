from collections import defaultdict
import sys

with open('7-input.txt') as f:
    lines = [line.rstrip() for line in f]

def parse_line(line):
    def get_contents(raw_contents):
        return list(map(lambda raw: ' '.join(raw.split()[1:3]), raw_contents))

    sentences = line.split(', ')
    first_part = sentences[0].split(' bags contain ')
    container = first_part[0]
    contents_raw = sentences[1:]
    contents = []
    if not first_part[1].startswith('no'):
        contents_raw.append(first_part[1])
        contents = get_contents(contents_raw)
    return container, contents

contained_in = defaultdict(list)
for line in lines:
    container, contents = parse_line(line)
    for content in contents:
        contained_in[content].append(container)

root = 'shiny gold'
visited = set()

def visit_containers(content):
    if content in visited:
        return
    visited.add(content)
    for container in contained_in[content]:
        visit_containers(container)

visit_containers(root)
# minus 1 for shiny gold itself
print(len(visited) - 1)
