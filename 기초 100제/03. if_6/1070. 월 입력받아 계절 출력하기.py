x = int(input().rstrip())

arr = [0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 0]

if arr[x-1] == 0:
    print('winter')
elif arr[x-1] == 1:
    print('spring')
elif arr[x-1] == 2:
    print('summer')
elif arr[x-1] == 3:
    print('fall')
