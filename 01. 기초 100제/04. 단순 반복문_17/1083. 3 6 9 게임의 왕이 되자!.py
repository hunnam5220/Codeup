s = int(input().rstrip())

for x in range(1, s+1):
    if x % 3 != 0:
        print(x, end=' ')
    else:
        print('X', end=' ')