T = int(input())
for ts in range(1, T+1):
    A = [[""]*10 for i in range(10)]
    N = int(input())
    for i in range(N):
        x = list(map(int, input().split()))
        if x[-1] == 1:
            for i in range(x[0], x[2]+1):
                for j in range(x[1], x[3]+1):
                    A[i][j] += "1"
        else:
            for i in range(x[0], x[2] + 1):
                for j in range(x[1], x[3] + 1):
                    A[i][j] += "2"
    # print(A)
    num = 0
    for i in range(10):
        for j in range(10):
            if ("1" in A[i][j]) and ("2" in A[i][j]):
                num += 1
    print(f"#{ts} {num}")

