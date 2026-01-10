x, y = map(int, input().split())

que = list()
que.append(x)
que.append(y)

an = 0
for _ in range(3, 11):
    an = int(str(que[0] + que[1])[::-1])
    que.pop(0)
    que.append(an)

print(an)
