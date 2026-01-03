n, m = map(int, input().split())
a = list(map(int, input().split()))

for i in range(n):
    tmp = a[:]
    tmp.remove(tmp[i])
    if sum(tmp) == m:
        print("Yes")
        exit()

print("No")
