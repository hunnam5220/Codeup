s = int(input().rstrip())
r = 0
for x in range(1, 47):
    r += x
    if r >= s:
        print(x)
        break
