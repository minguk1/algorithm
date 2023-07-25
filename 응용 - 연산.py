from collections import deque


def bfs(n, m):
    visit[n] = 1
    q = deque()
    q.append(n)

    while q:
        v = q.popleft()
        if v == m:
            return visit[v]
        for i in (v + 1, v - 1, v * 2, v - 10):
            if 0 < i < 1000001 and visit[i] == 0:
                q.append(i)
                visit[i] = visit[v] + 1

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    visit = [0] * 1000001

    print(f"#{tc} {bfs(n, m)-1}")

