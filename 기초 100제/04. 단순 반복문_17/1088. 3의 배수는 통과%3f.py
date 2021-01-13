n = int(input().rstrip())

for x in range(1, n+1):
    if x % 3 == 0:
        continue

    else:
        print(x, end=' ')