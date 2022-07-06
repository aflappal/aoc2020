import sys

with open('9-input.txt') as f:
    lines = [line.rstrip() for line in f]

nums = [int(line) for line in lines]
test_nums = [
        35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102,
        117, 150, 182, 127, 219, 299, 277, 309, 576
        ]

act_nums = nums
win_len = 25
print(act_nums)

def find_sum(win, num_to_find):
    for i in range(len(win)-1):
        num1 = win[i]
        for num2 in win[i+1:]:
            if num1 + num2 == num_to_find:
                return True
    return False

for i in range(win_len, len(act_nums)):
    win = act_nums[i-win_len:i]
    num = act_nums[i]
    print(i, num)
    print(win)
    if not find_sum(win, num):
        print(f'{num} can\'t be summed')
        break
else:
    print('All could be summed!')
