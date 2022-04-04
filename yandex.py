n, m = map(int, input().split())
month = [0] * n

if m != 0 and n != 0:
    for i in range(m):
        l, r, x = map(int, input().split())
        for j in range(l-1, r):
            if month[j] < x:
                month[j] = x

    print(sum(month))
else:
    print(0)

'''
10 3
1 5 5
6 10 6
3 7 7
'''

'''
3 4
1 2 2
2 3 3
2 2 1
2 2 4
'''