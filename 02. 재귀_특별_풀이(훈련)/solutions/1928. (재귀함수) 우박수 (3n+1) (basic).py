from sys import stdin


def solutions(n, cnt):
    if cnt == 0:
        print(n)
        cnt += 1
    if n == 1:
        return
    if n % 2 == 0:
        n /= 2
        print(int(n))
        return solutions(n, cnt)
    else:
        n = 3 * n + 1
        print(int(n))
        return solutions(n, cnt)

cnt = 0
solutions(int(stdin.readline().rstrip()), cnt)
