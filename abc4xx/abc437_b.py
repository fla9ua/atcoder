h, w, n = map(int, input().split())
a = list((input() for _ in range(h)))
b = list(map(int, (input() for _ in range(n))))

bing = list()
for i in a:
    cnt = 0
    for j in i.split():
        if int(j) in b:
            cnt += 1
    bing.append(cnt)

print(max(bing))