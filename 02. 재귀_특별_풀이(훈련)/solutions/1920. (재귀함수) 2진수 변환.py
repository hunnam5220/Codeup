from sys import stdin

def solutions(n, arr):
    if n // 2 == 1 and n % 2 == 0:
        arr.append(0)
        arr.append(1)
        return arr

    elif n // 2 == 1 and n % 2 == 1:
        arr.append(1)
        arr.append(1)
        return arr

    if n % 2 == 0:
        arr.append(0)
        return solutions(n // 2, arr)
    else:
        arr.append(1)
        return solutions(n // 2, arr)

n = int(stdin.readline().rstrip())
arr = []

if n // 2 != 0:
    print(''.join(list(map(str, reversed(solutions(n, arr))))))
else:
    print(n)