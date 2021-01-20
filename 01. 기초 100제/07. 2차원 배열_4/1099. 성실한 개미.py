arr = []
for x in range(10):
    arr.append(list(map(int, input().split())))

s_x, s_y = 1, 1
chk = False

for x in range(1, len(arr)-1):
    if arr[s_x][s_y] == 2:
        arr[s_x][s_y] = 9
        break

    for y in range(1, len(arr)):
        if arr[s_x][s_y] == 1:
            s_x+=1
            break

        elif arr[s_x][s_y] == 2:
            arr[s_x][s_y] = 9
            chk = True
            break

        else:
            arr[s_x][s_y] = 9
            s_y += 1

    if chk:
        break

    if arr[s_x][s_y-1] == 2:
        arr[s_x][s_y - 1] = 9
        break

    if arr[s_x][s_y-1] != 1:
        arr[s_x][s_y - 1] = 9

for x in arr:
    for y in x:
        print(y, end=' ')
    print()