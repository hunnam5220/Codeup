from sys import stdin


def functions(n):
    b_num = 1
    d_num = int(bin(b_num)[2:])

    while True:
        if d_num % n == 0:
            return d_num

        b_num += 1
        d_num = int(bin(b_num)[2:])

        if d_num >= 100000000000000000000:
            return 0


print(functions(int(stdin.readline().rstrip())))