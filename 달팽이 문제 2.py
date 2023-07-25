dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T+1):
    n = int(input())

    snail = [[0] * n for _ in range(n)]
    #현재 위치
    r, c = 0, 0

    d = 0

    for i in range(1, n*n + 1):
        snail[r][c] = i
        nr = r + dr[d]
        nc = c + dc[d]

        if 0 <= nr < n and 0 <= nc < c and snail[nr][nc] == 0:
            r, c = nr, nc
        else:
            d += 1
            if d == 4:
                d = 0
            r = r + dr[d]
            c = c + dc[d]

    print(snail)