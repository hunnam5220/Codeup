from sys import stdin


def functions(arr, x, y, n):
    if x < 0 or x > 6 or y < 0 or y > 6:
        return False

    # while True:

        


arr = []
x, y = 0, 0

for step in range(7):
    arr.append(list(map(int, stdin.readline().rstrip().split())))

for n in range(1, 6):
    functions(arr, x, y, n)