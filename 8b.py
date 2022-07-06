import sys

with open('8-input.txt') as f:
    lines = [line.rstrip() for line in f]


class Machine:
    def __init__(self, code):
        self.code = code
        self.accu = 0
        self.ip = 0
        self.executed = set()

    def run(self):
        while self.ip not in self.executed:
            self.executed.add(self.ip)
            cmd, off = self.code[self.ip]
            if cmd == 'jmp':
                self.ip += off
            elif cmd == 'acc':
                self.accu += off
                self.ip += 1
            elif cmd == 'nop':
                self.ip += 1
            else:
                raise RuntimeError('Unknown command')
            if self.ip == len(self.code):
                return 'term'
        return 'loop'


test_lines = [
        'nop +0',
        'acc +1',
        'jmp +4',
        'acc +3',
        'jmp -3',
        'acc -99',
        'acc +1',
        'jmp -4',
        'acc +6'
        ]

code = []
for line in lines:
    cmd, off_string = line.split()
    code.append((cmd, int(off_string)))

for i, ins in enumerate(code):
    cmd, off = ins
    if cmd == 'acc':
        continue
    mod_code = code.copy()
    assert mod_code == code
    if cmd == 'nop':
        mod_code[i] = ('jmp', off)
    elif cmd == 'jmp':
        mod_code[i] = ('nop', off)
    assert mod_code != code
    machine = Machine(mod_code)
    ret = machine.run()
    if ret == 'term':
        print(machine.accu)
        break
else:
    print('No program terminated!')
