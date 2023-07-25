from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T+1):

    n, m = map(int, input().split())

    water_list = deque()
    visit = [[-1] * m for _ in range(n)]


    for i in range(n):
        row = list(input())
        for j in range(len(row)):
            if row[j] == "W":
                water_list.append((i, j))
                visit[i][j] = 0

    dis_sum = 0
    while water_list:
        i, j = water_list.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<n and 0<=nj<m and visit[ni][nj] == -1:
                water_list.append((ni, nj))
                visit[ni][nj] = visit[i][j] + 1
                dis_sum += visit[ni][nj]

    print(f"#{tc} {dis_sum}")


