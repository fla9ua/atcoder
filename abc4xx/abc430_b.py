n, m = map(int, input().split())
s = list(input() for _ in range(n))
t = set()

for i in range(n - m + 1):
    for j in range(n - m + 1):
        t.add(tuple(s[k][j:j + m] for k in range(i, i + m)))

print(len(t))
