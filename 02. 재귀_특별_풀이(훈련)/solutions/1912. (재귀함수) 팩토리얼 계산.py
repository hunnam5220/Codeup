from sys import stdin

def functions(n):
    if n != 1:
        return functions(n-1) * n
    else:
        return n

print(functions(int(stdin.readline().rstrip())))