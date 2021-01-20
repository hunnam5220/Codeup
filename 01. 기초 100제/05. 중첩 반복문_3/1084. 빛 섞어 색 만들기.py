i, j, k = input().split()
i, j, k = int(i), int(j), int(k)

cnt = 0
for x in range(i):
    for y in range(j):
        for z in range(k):
            print(x, y, z)
            cnt+=1

print(cnt)