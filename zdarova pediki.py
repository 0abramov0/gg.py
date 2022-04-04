t = int(input())
ans = []

for i in range(t):
    n, k = map(int, input().split())
    a = []
    for j in range(n):
        a.append(input())

    seta = set(a)
    if len(a) != len(seta) and len(seta) == 1:
        ans.append('YES')
        continue

    for x in range(k):
        s = 0
        check = True
        for y in range(n):
            s += int(a[y][x])
        if s % 2 != 0 and s != n:
            ans.append('NO')
            check = False
            break
        if check and x == k-1:
            ans.append('YES')



for line in ans:
    print(line)


'''
3
3 3
110
100
110
'''