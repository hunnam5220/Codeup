w, h = input().split()
w, h = int(w), int(h)

n = int(input().rstrip())

arr = [[0]*h for x in range(w)]

for step in range(n):
    l, d, x, y = input().split()
    l, d, x, y = int(l), int(d), int(x)-1, int(y)-1

    for i in range(l):
        if d:
            arr[x+i][y] = 1
        else:
            arr[x][y+i] = 1

for i in arr:
    for k in i:
        print(k, end=' ')
    print()