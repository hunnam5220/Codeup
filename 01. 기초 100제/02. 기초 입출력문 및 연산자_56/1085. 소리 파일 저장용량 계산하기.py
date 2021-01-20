arr = list(map(int, input().split()))
result = 1
for x in arr:
    result *= x

print("%.2f MB" % (result/8/1024/1024))