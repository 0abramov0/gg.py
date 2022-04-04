t = int(input())
ans = []

for i in range(t):
    n, k = map(int, input().split())
    a = []
    p = []
    for j in range(n):
        a.append(input())

    seta = set(a)
    if len(a) != len(seta) and len(seta) == 1:
        ans.append('YES')
        continue

    for y in range(k):
        s = 0
        for x in range(n):
            s += int(a[x][y])
        if s % 2 == 0:
            p.append(True)

    if len(p) == k:
        ans.append('YES')
    else:
        ans.append('NO')

for item in ans:
    print(item)
