T = int(input())

for tc in range(1, T+1):
    n = int(input())

    arr = [list(map(int, input().split())) for _ in range(n)]

    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            # i, j 위치에서 위에서도 올 수 있고, 왼쪽에서도 올 수 있다.
            if i-1 >= 0 and j-1 >= 0:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + arr[i][j]

            # 위에서만 올 수 있다.
            if i -1 >= 0 and j - 1 < 0:
                dp[i][j] = dp[i-1][j] + arr[i][j]

            # 왼쪽에서만 올 수 있다.
            if i - 1 < 0 and j - 1 >= 0:
                dp[i][j] = dp[i][j-1] + arr[i][j]

            # 두 방향 다 오지 못한다.
            elif i - 1 < 0 and j - 1 < 0:
                dp[i][j] = arr[i][j]

    print(f"{tc} {dp[n-1][n-1]}")


