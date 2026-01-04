n = int(input())
l = list(map(int, input().split()))

a = 0
for i in range(n):
    if l[i] == 1:
        break
    a += 1

b = n
for j in range(n - 1, -1, -1):
    if l[j] == 1:
        break
    b -= 1

print(max(0, b - a - 1))
