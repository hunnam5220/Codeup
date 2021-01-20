from sys import stdin


def functions(a, b):
    if a > b:
        return

    if b % 2 != 0:
        return functions(a, b-1), print(b)
    else:
        return functions(a, b-1)


a, b = map(int, stdin.readline().split())

functions(a, b)