t = int(input())

n = list()
w = list()
output = []
for _ in range(t):
    n, w = map(int, input().split())
    c = [int(i) for i in input().split()]

    min_cost = []
    x = 1
    while x <= 2 * w:
        s = 0
        for i in range(1, n + 1):
            if (i + x) % (2 * w) < w:
                s += int(c[i - 1])
        min_cost.append(s)
        x += 1

    min_cost.sort()
    output.append(min_cost[0])

print(*output)
