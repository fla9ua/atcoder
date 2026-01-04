s = input()

cnt = dict()
for i in s:
    cnt[i] = cnt.get(i, 0) + 1

for j in cnt:
    if cnt[j] == 1:
        print(j)
        break
