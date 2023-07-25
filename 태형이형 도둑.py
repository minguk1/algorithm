def bfs(r, c, arr):
    visited = [[0]*m for _ in range(n)]
    q = []
    q.append((r, c))
    visited[r][c] = 1

    while q:
        y, x = q.pop(0)
        for i in pi[arr[y][x]]:
            yy = y + dy[i]
            xx = x + dx[i]
            if 0<=yy<n and 0<=xx<m and visited[yy][xx] == 0 and (i+2)%4 in pi[arr[yy][xx]]:
                q.append((yy, xx))
                visited[yy][xx] = visited[y][x] +1
    return visited
dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]
pi = [[],[0, 1, 2, 3],[0, 2],[1, 3],[0,3],[2,3],[1,2],[1,2]]

T = int(input())
for tc in range(1, T+1):
    n, m, r, c, time = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    cnt = 0
    visited = bfs(r, c, arr)
    # print(visited)
    for i in range(n):
        for j in range(m):
            if visited[i][j] <= time and visited[i][j] != 0:
                cnt += 1
    print(f'#{tc} {cnt}')