n = int(input())
t = list(map(int, input().split()))

result = dict()

for i in range(n):
    result[t[i]] = i + 1

output = sorted(result.items(), key=lambda x: x[0])[:3]

print(*[i[1] for i in output])
