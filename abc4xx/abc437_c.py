t = int(input())

for _ in range(t):
    wp = []
    n = int(input())
    for i in range(n):
        wp.append(list(map(int, input().split())))
    wp.sort(key=lambda x: (x[0] + x[1]))

    sum_p = 0
    for w, p in wp:
        sum_p += p

    res = 0
    for i in range(n):
        w, p = wp[i]
        res += w + p
        if sum_p < res:
            print(i)
            break
