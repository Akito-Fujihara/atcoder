# https://atcoder.jp/contests/joi2008ho/submissions/me

from itertools import product
from bisect import bisect

N, M = (int(x) for x in input().split())

numbers = [0]

for _ in range(N):
    numbers.append(int(input()))

p = set()
for i, j in product(range(N + 1), repeat=2):
    p.add(numbers[i] + numbers[j])
p = list(sorted(p))
ans = 0
for i in p:
    index = bisect(p, M - i)
    if index == 0:
        continue
    ans = max(ans, i + p[index - 1])

print(ans)
