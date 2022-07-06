import sys

with open('8-input.txt') as f:
    lines = [line.rstrip() for line in f]

code = []
for line in lines:
    cmd, off_string = line.split()
    code.append((cmd, int(off_string)))
accu = 0
ip = 0

executed = []

while ip not in executed:
    executed.append(ip)
    cmd, off = code[ip]
    if cmd == 'jmp':
        ip += off
    elif cmd == 'acc':
        accu += off
        ip += 1
    elif cmd == 'nop':
        ip += 1
    else:
        raise RuntimeError('Unknown command')
    print(f'{cmd} {off}; after accu {accu}')
