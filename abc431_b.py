x = int(input())
n = int(input())
w = list(map(int, input().split()))
q = int(input())
p = list(map(int, (input() for _ in range(q))))

done = []
for i in range(q):
    if p[i] in done:
        x -= w[p[i] - 1]
        done.remove(p[i])
    else:
        x += w[p[i] - 1]
        done.append(p[i])

    print(x)
