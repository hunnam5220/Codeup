arr = [0] * 23

n = int(input().rstrip())
nums = list(map(int, input().split()))

for x in nums:
    arr[x-1] += 1

for x in arr:
    print(x, end=' ')