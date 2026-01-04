n, m, k = map(int, input().split())

e = {}
ans = []

for i in range(k):
    a, b = map(int, input().split())
    e[a] = e.get(a, [])
    e[a].append(b)
    if len(e[a]) == m:
        ans.append(a)

print(*ans)
