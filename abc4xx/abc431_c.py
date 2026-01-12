n, m, k = map(int, input().split())
h = list(map(int, input().split()))
b = list(map(int, input().split()))

h.sort()
b.sort()

print("Yes") if all(h <= b for h, b in zip(h[:k], b[-k:])) else print("No")
