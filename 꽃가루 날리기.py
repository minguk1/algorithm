T = int(input())
for ts in range(1, T+1):

    N, M = map(int, input().split())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    # print(A)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    sum_list = []
    for x in range(N):
        for y in range(M):
            now = A[x][y]
            now_sum = A[x][y]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < M:
                    now_sum += A[nx][ny]
            sum_list.append(now_sum)
    print(f"#{ts} {max(sum_list)}")