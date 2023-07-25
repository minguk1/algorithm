T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())

    arr = [[0]*(n+2) for _ in range(n+2)]

    k = n//2
    arr[k][k] = arr[k+1][k+1] = 2
    arr[k+1][k] = arr[k][k+1] = 1

    for _ in range(m):
        si, sj, d = map(int, input().split())
        arr[si][sj] = d
        for di, dj in ((-1, -1),(-1, 0), (-1, 1),(0, 1),(1, 1),(1, 0),(1, -1),(0, -1)):
            tlst = []
            for mul in range(1, n):
                ni, nj = si+di*mul, sj+dj*mul
                if arr[ni][nj] == 0:
                    break
                elif arr[ni][nj] != d:
                    tlst.append((ni, nj))
                else:
                    while tlst:
                        ti, tj = tlst.pop()
                        arr[ti][tj] = d
                    break

    bcnt = wcnt = 0
    for lst in arr:
        bcnt += lst.count(1)
        wcnt += lst.count(2)
    print(f"#{tc} {bcnt} {wcnt}")