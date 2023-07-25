
def kill(A, m, i, j):
    kill_sum = 0
    for a in range(m):
        for b in range(m):
            if 0 <= i+a < n and 0 <= j + b < n:
                kill_sum += A[i+a][j+b]

    return kill_sum
T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    fly = [0] * n

    for i in range(n):
        fly[i] = list(map(int, input().split()))

    max_fly = 0
    for i in range(n):
        for j in range(n):
            if kill(fly, m, i, j) > max_fly:
                max_fly = kill(fly, m, i, j)

    print(f"#{tc} {max_fly}")