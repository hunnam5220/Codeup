from sys import stdin


def to_n(n, a):
    if n != a:
        return to_n(n, a + 1), print(a)
    else:
        return print(n)


n = int(stdin.readline().rstrip())
a = 1
to_n(n, a)