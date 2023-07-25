from collections import deque
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def bfs():
    q = deque()
    q.append((0,0))

    v = [[999999]*n for i in range(n)]
    v[0][0] = 0

    while q:
        i, j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]

            if 0 <= ni < n and 0 <= nj < n and v[ni][nj] > v[i][j] + max((height[ni][nj] - height[i][j]),0) + 1:
                if height[ni][nj] > height[i][j]:
                    t = v[i][j] + (height[ni][nj] - height[i][j]) + 1
                    v[ni][nj] = min(v[ni][nj], t)
                else:
                    t = v[i][j] + 1
                    v[ni][nj] = min(v[ni][nj], t)
                q.append((ni, nj))
    # print(v)
    # print(v[n-1][n-1])
    return v[n-1][n-1]

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    height = [0] * n
    for i in range(n):
        height[i] = list(map(int, input().split()))

    # bfs()
    print(f"#{tc} {bfs()}")