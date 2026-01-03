s, a, b, x = map(int, input().split())

length = 0
length += (x // (a + b)) * a
length += min(x % (a + b), a)
print(length * s)
