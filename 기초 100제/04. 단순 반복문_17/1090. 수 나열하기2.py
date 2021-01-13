arr = list(map(int, input().split()))
r = arr[0]
for x in range(arr[2]-1):
    r *= arr[1]

print(r)