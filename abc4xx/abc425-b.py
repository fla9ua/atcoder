n = int(input())
a = list(map(int, input().split()))

used = [0] * (n + 1)
for i in range(n):
	if a[i] >= 0:
		if used[a[i]]:
			print("No")
			exit()
		used[a[i]] = True

piv = 1
for i in range(n):
	if a[i] == -1:
		while used[piv]:
			piv += 1
		used[piv] = True
		a[i] = piv

print("Yes")
print(*a)
