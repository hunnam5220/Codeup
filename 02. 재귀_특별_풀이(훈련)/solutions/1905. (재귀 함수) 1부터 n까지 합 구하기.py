from sys import stdin
import sys
sys.setrecursionlimit(1000000)

def functions(n):
    if n != 1:
        return functions(n-1) + n
    else:
        return n

result = functions(int(stdin.readline().rstrip()))

print(result)