import sys

with open('10-input.txt') as f:
    lines = [line.rstrip() for line in f]

nums = [int(line) for line in lines]
test_nums = [ 16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4 ]

act_nums = sorted(nums)
print(act_nums)

prev = 0
counts = [None, 0, 0, 0]

for num in act_nums:
    diff = num - prev
    counts[diff] += 1
    prev = num

# built-in adapter is 3 jolts higher than biggest
counts[3] += 1
print(counts[1:])
_, ones, _, threes = counts

# final answer
print(ones * threes)
