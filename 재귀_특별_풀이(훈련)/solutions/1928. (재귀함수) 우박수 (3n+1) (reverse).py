from sys import stdin


def solutions(n):
    if n == 1:
        return print(int(n))

    if n % 2 == 0:
        return solutions(n / 2), print(int(n))

    else:
        return solutions(3 * n + 1), print(int(n))


solutions(int(stdin.readline().rstrip()))