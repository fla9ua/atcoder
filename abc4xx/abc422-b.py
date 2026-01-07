h, w = map(int, input().split())
s = list(input() for _ in range(h))

cell = [[1, 0], [-1, 0], [0, 1], [0, -1]]

for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            cnt = 0
            for k in cell:
                x, y = i + k[1], j + k[0]
                if 0 <= x < h and 0 <= y < w and s[x][y] == "#":
                    cnt += 1
            if cnt != 2 and cnt != 4:
                print("No")
                exit()

print("Yes")
