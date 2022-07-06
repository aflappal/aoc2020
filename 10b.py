from collections import defaultdict
import sys

with open('10-input.txt') as f:
    lines = [line.rstrip() for line in f]

nums = [int(line) for line in lines]
test_nums = [ 16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4 ]
test_nums2 = [ 28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38,
               39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3 ]

act_nums = [0] + sorted(nums)
print(act_nums)
branches_after = defaultdict(int)
branches_after[act_nums[-1] + 3] = 1

for num in reversed(act_nums):
    branches_after[num] = sum(branches_after[num+i] for i in [1, 2, 3])

print(branches_after[0])
