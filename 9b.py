import sys

with open('9-input.txt') as f:
    lines = [line.rstrip() for line in f]

nums = [int(line) for line in lines]
target = 27911108

test_nums = [
        35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102,
        117, 150, 182, 127, 219, 299, 277, 309, 576
        ]
test_target = 127

act_nums = nums
act_target = target
print(act_nums)

# Have to find contiguous sequence of numbers summing to target. Idea: sum a
# moving window with changing size. If sum is too small then extend window at
# the end. If sum is too large then shrink it from the front. This way all
# sequences will be covered.
front = 0
end = 2
cursum = act_nums[0] + act_nums[1]
# invariant: at start of iteration cursum == sum(act_nums[front:end])
while end <= len(act_nums):
    #assert cursum == sum(act_nums[front:end])
    if cursum < act_target:
        cursum += act_nums[end]
        end += 1
    elif cursum > act_target:
        cursum -= act_nums[front]
        front += 1
        # make sure we're always summing at least two numbers
        if front == end:
            end += 1
    else:
        # We found our sequence
        win = act_nums[front:end]
        min_win = min(win)
        max_win = max(win)
        # The actual answer
        print(min_win + max_win)
        assert sum(win) == act_target, (sum(win), act_target)
        break
else:
    print('Couldn\'t find sum!')
