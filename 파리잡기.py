def kill_fly(A, i, j, m):
    fly = 0
    for k in range(m):
        for l in range(m):
            fly += A[i+k][j+l]
    return fly
T = int(input())
for ts in range(1, T+1):
    N, M = map(int, input().split())
    A = [0]*N
    for i in range(N):
        A[i] = list(map(int, input().split()))
    # print(A)
    fly_max = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            kill = kill_fly(A, i, j, M)
            # print(kill)
            if kill > fly_max:
                fly_max = kill

    print(f"#{ts} {fly_max}")