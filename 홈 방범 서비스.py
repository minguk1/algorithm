T = int(input())
for tc in range(1, T+1):

    N, M = map(int, input().split())
    city = [0] * N
    for i in range(N):
        city[i] = list(map(int, input().split()))
    for k in range(N+1, 0, -1):
        max_cnt = 0
        max_home = 0
        for i in range(N):
            for j in range(N):
                # print(f"start {i}{j}")
                cnt = 0
                home = 0
                visit = [[0]*N for _ in range(N)]


                if city[i][j] == 1:
                    cnt += M
                    home += 1
                    visit[i][j] = 1
                visit = [[0]*N for _ in range(N)]
                for t in range(1, k):
                    for m in range(0, t+1):
                        n = t - m
                        # print(f"m {m} n {n}")
                        if 0 <= i + m < N and 0 <= j + n < N and city[i+m][j+n] == 1 and not visit[i+m][j+n]:
                            cnt += M
                            home += 1
                            visit[i+m][j+n] = 1
                            # print(i, j,i + m, j + n, home)
                            # print(1)
                        if 0 <= i + m < N and 0 <= j - n < N and city[i+m][j-n] == 1 and not visit[i + m][j - n]:
                            cnt += M
                            home += 1
                            visit[i + m][j - n] = 1
                            # print(i, j,i + m, j - n, home)
                            # print(2)
                        if 0 <= i - m < N and 0 <= j - n < N and city[i-m][j-n] == 1 and not visit[i - m][j - n]:
                            cnt += M
                            home += 1
                            visit[i - m][j - n] = 1
                            # print(i, j,i - m, j - n, home)
                            # print(3)
                        if 0 <= i - m < N and 0 <= j + n < N and city[i-m][j+n] == 1 and not visit[i - m][j + n]:
                            cnt += M
                            home += 1
                            visit[i - m][j + n] = 1
                            # print(i, j,i - m, j + n, home)
                            # print(4)
                if cnt >= max_cnt:
                    max_cnt = cnt
                    # print(i, j, home)
                if home >= max_home:
                    max_home = home
        if max_cnt >= k**2 + (k-1)** 2:
            # print(max_cnt, max_home)
            # print(k)
            print(f"#{tc} {max_home}")
            break

