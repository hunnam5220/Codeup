arr = [[0]*19 for x in range(19)]
n = int(input().rstrip())

for step in range(n):
    x, y = input().split()
    x, y = int(x), int(y)

    arr[x-1][y-1] = 1

for x in arr:
    for y in x:
        print(y, end=' ')
    print()