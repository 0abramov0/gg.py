slave = input()
a = [[0 for _ in range(102)] for _ in range(102)]
dick = []
for i in slave:
    dick.append(i)


def robot():
    x = 51
    y = 51
    a[x][y] = 1
    pos = 'u'
    steps = 1

    for cum in dick:
        if cum == 'S':
            if pos == 'u':
                if a[x][y + 1] == 1:
                    print(steps)
                    return
                else:
                    y += 1
                    a[x][y] = 1
            elif pos == 'd':
                if a[x][y - 1] == 1:
                    print(steps)
                    return
                else:
                    y -= 1
                    a[x][y] = 1
            elif pos == 'r':
                if a[x + 1][y] == 1:
                    print(steps)
                    return
                else:
                    x += 1
                    a[x][y] = 1
            elif pos == 'l':
                if a[x - 1][y] == 1:
                    print(steps)
                    return
                else:
                    x -= 1
                    a[x][y] = 1
            steps += 1

        elif cum == 'R':
            if pos == 'u':
                pos = 'r'
            elif pos == 'r':
                pos = 'd'
            elif pos == 'd':
                pos = 'l'
            elif pos == 'l':
                pos = 'u'

        elif cum == 'L':

            if pos == 'u':
                pos = 'l'
            elif pos == 'r':
                pos = 'u'
            elif pos == 'd':
                pos = 'r'
            elif pos == 'l':
                pos = 'd'

    print(-1)


robot()