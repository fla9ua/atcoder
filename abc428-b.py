n, k = map(int, input().split())
s = input().strip()

memo = dict()

for i in range(n - k + 1):
    t = s[i:i + k]
    memo[t] = memo.get(t, 0) + 1

vmax = 0
for val in memo.values():
    vmax = max(vmax, val)

vs = []
for key, val in memo.items():
    if val == vmax:
        vs.append(key)

vs.sort()

print(vmax)
print(" ".join(vs))
