arr = list(map(int, input().split()))
r = arr[0]
for x in range(arr[3]-1):
    r *= arr[1]
    r += arr[2]

print(r)