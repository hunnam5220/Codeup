arr = [0] * 23

n = int(input().rstrip())
nums = list(map(int, input().split()))

for x in reversed(nums):
    print(x, end=' ')