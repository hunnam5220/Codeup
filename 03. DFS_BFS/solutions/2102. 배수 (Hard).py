n = int(input())


def find_multiple_js(n):
    b_num = 0b1
    d_num = int(format(b_num, "b"), 10)

    while 1:
        if d_num % n == 0:
            return d_num
        b_num += 1
        d_num = int(format(b_num, "b"), 10)

        if d_num >= 100000000000000000000:
            return 0


print(find_multiple_js(n))