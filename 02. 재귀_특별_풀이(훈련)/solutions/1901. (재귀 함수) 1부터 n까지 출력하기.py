from sys import stdin


def to_n(a, n):
    if n != a:
        return to_n(a, n - 1), print(n)
    else:
        return print(a)


n = int(stdin.readline().rstrip())
a = 1
to_n(a, n)