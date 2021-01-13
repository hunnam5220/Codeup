from sys import stdin

def solutions(n, f, s):
    if n > 2:
        tmp = f
        f += s
        s = tmp
        return solutions(n-1, f, s)
    else:
        return f+s

f, s = 1, 0
print(solutions(int(stdin.readline().rstrip()), f, s))