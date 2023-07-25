di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T+1):

    m, n, p = map(int, input().split())

    farm = [[0]*n for _ in range(m)]
    visit = [[0]*n for _ in range(m)]

    for i in range(p):
        a, b = map(int, input().split())
        farm[a][b] = 1

    for i in range(m):
        for j in range(n):
            if farm[i][j] == 1 and visit[i][j] == 0:
                stack = [[i, j]]
                visit[i][j] = 1
                # print(stack)
                while stack:
                    t = stack[0][0]
                    s = stack.pop(0)[1]

                    for k in range(4):
                        nt = t + di[k]
                        ns = s + dj[k]

                        if 0 <= nt < m and 0 <= ns < n and farm[nt][ns] == 1 and visit[nt][ns] == 0:
                            # print(nt, ns)
                            visit[nt][ns] = visit[t][s] + 1
                            stack.append([nt, ns])
                            # print(stack)
    # for i in visit:
    #     print(i)

    result = 0
    for i in visit:
        result += i.count(1)
    print(result)