n = int(input())


def func(x):
    sum = 0
    for i in str(x):
        sum += int(i)
    return sum


a = 1
for _ in range(n - 1):
    a += func(a)

print(a)
