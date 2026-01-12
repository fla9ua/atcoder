n, a, b = map(int, input().split())
s = input()

aa = [0] * (n + 1)
bb = [0] * (n + 1)
for i in range(n):
    aa[i + 1] = aa[i] + (1 if s[i] == 'a' else 0)
    bb[i + 1] = bb[i] + (1 if s[i] == 'b' else 0)

cnt = 0

for i in range(1, n):
    left = i
    right = n
    while left <= right:
        mid = (right + right) // 2
        if a <= (aa[mid] - aa[i]):
            right = mid
        else:
            left = mid
    left = right

    if left > n:
        continue

    l = i - 1
    r = n + 1
    while abs(l - r) > 1:
        m = (l + r) // 2
        if (bb[m] - bb[i]) < b:
            l = m
        else:
            r = m
    right = l

    cnt += max(right - left + 1, 0)

print(cnt)
