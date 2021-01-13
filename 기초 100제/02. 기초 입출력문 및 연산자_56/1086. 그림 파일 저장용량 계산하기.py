arr = list(map(int, input().split()))
result = 1
for x in arr:
    result *= x

print("%.1f MB" % (result/8/1024/1024))