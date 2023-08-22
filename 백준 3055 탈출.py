from collections import deque

m, n = map(int, input().split())
arr = [[0] * n for _ in range(m)]
back = [0] * m
visit = [[0] * n for _ in range(m)]
water = deque()
q = deque()
x,y = 0,0
for i in range(m):
    back[i] = list(input())

start = (0, 0)
arrive = False
for i in range(m):
    for j in range(n):
        if back[i][j] == 'D':
            arr[i][j] = 900
            x,y = i, j
        elif back[i][j] == '*':
            arr[i][j] = -1
            water.append((i,j))
            visit[i][j] = -1
        elif back[i][j] == 'S':
            arr[i][j] = 1
            visit[i][j] = 1
            q.append((i,j))
        elif back[i][j] == 'X':
            arr[i][j] = 'x'

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def bfs(now_q, now_water):
    global arrive
    next_water = deque()
    next_q = deque()
    while now_water:
        a, b = now_water.popleft()

        for k in range(4):
            next_a = a + di[k]
            next_b = b + dj[k]
            if 0 <= next_a < m and 0 <= next_b < n and visit[next_a][next_b] == 0 and arr[next_a][next_b] != 'x' and arr[next_a][next_b] != 900:
                visit[next_a][next_b] = visit[a][b] - 1
                next_water.append((next_a, next_b))
    # print(visit)



    while now_q:
        s, t = now_q.popleft()

        for k in range(4):
            next_s = s + di[k]
            next_t = t + dj[k]
            if 0 <= next_s < m and 0 <= next_t < n and visit[next_s][next_t] == 0 and arr[next_s][next_t] != 'x':
                visit[next_s][next_t] = visit[s][t] + 1
                next_q.append((next_s, next_t))
                if arr[next_s][next_t] == 900:
                    arrive = True
                    return
    if len(next_q) == 0:
        return

    # print(visit)
    bfs(next_q, next_water)

bfs(q,water)

if arrive == True:
    print(visit[x][y]-1)
else:
    print("KAKTUS")



