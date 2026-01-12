# input
a, b, c, n = map(int, input().split())
s = list(input() for _ in range(a))

# algorithm

"""
累積和（prefix sum）
ps[i] = A[0] + A[1] + ... + A[i-1]
"""
A = [3, 1, 4, 1, 5, 9]
ps = [0] * (len(A) + 1)
for i in range(len(A)):
    ps[i + 1] = ps[i] + A[i]

print(ps)


"""
二文探索
"""
def binary_search(arr, x):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# or

import bisect

X = 10
idx = bisect.bisect_left(ps, X)
print(idx)