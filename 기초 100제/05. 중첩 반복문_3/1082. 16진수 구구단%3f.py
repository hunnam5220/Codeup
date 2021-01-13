n = input().rstrip()

for x in range(1, 16):
    print("%s*%X=%X"% (n, x, int(n, 16)*x))