arr = []

for x in range(19):
    arr.append(list(map(int, input().split())))

n = int(input().rstrip())

for step in range(n):
    x, y = input().split()
    x, y = int(x)-1, int(y)-1

    for yy in range(19):
        if arr[x][yy] == 0:
            arr[x][yy] = 1
        else:
            arr[x][yy] = 0

    for xx in range(19):
        if arr[xx][y] == 0:
            arr[xx][y] = 1
        else:
            arr[xx][y] = 0

for x in arr:
    for y in x:
        print(y, end=' ')
    print()