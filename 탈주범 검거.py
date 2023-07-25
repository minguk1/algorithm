#상좌하우
di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]

def cango(k, a, b):
    if a == 2:
        if k == 0: #상 방향
            if b == 3 or 4 or 7:
                return False
        elif k == 2: #하 방향
            if b == 3 or 5 or 6:
                return False

def direction(a):
    if a == 1:

        return [0, 1, 2, 3]
    elif a == 2:
        return [0, 2]
    elif a == 3:
        return [1, 3]
    elif a == 4:
        return [0, 3]
    elif a == 5:
        return [2, 3]
    elif a == 6:
        return [1, 2]
    elif a == 7:
        return [0, 1]
T = int(input())
for tc in range(1, T+1):
    n, m, r, c, l = map(int, input().split())

    ground = [0] * n
    for i in range(n):
        ground[i] = list(map(int, input().split()))
    visit = [[0]*m for _ in range(n)]
    q = []
    q.append((r, c))
    visit[r][c] = 1

    while q:
        now_i, now_j = q.pop(0)

        for k in direction(ground[now_i][now_j]):
            next_i = now_i + di[k]
            next_j = now_j + dj[k]
            if 0<=next_i<n and 0<=next_j<m and ground[next_i][next_j] != 0 and not visit[next_i][next_j] and ((k-2) in direction(ground[next_i][next_j]) or (k+2) in direction(ground[next_i][next_j])):
                q.append((next_i,next_j))
                visit[next_i][next_j] = visit[now_i][now_j] + 1
                if visit[next_i][next_j] == l + 1:
                    q = []
                    break

    # print(visit)
    cnt = 0
    for i in range(n):
        for j in range(m):
            if 0 < visit[i][j] <= l:
                # print(i, j)
                cnt += 1
    print(f"#{tc} {cnt}")