n = int(input())
s = list(input() for _ in range(n))
x, y = input().split()

print("Yes" if s[int(x) - 1] == y else "No")
