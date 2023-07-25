T = int(input())
for ts in range(1, T+1):

    N, K = map(int, input().split())
    A = [0]*N
    for i in range(N):
        A[i] = input().split()
    # print(A)
    a = [0]*N
    for i in range(N):
        a[i] = ''.join(A[i]).split("0")
    # print(a)
    B = [[0]*N for i in range(N)]
    for i in range(N):
        for j in range(N):
            B[i][j] = A[N-1-j][i]
    # print(B)
    b = [0]*N
    for i in range(N):
        b[i] = ''.join(B[i]).split("0")
    # print(b)
    cnt = 0
    # print(len(a), len(b))

    for i in range(len(a)):
        # print(a[i])
        # print(a[i].count("1"*K))
        cnt += a[i].count("1"*K)
        # print(cnt)
    for i in range(len(b)):
        # print(b[i])
        # print(b[i].count("1"*K))
        cnt += b[i].count("1"*K)
        # print(cnt)
    print(f"#{ts} {cnt}")
