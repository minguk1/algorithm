T = int(input())
for tc in range(1, T+1):

    n, m = map(int, input().split())
    A = [0]*n
    for i in range(n):
        A[i] = list(map(int, input().split()))

    di = [-1, 1, 0, 0, -1, 1, 1, -1]
    dj = [0, 0, -1, 1, 1, 1, -1, -1]
    max_fly = 0
    for i in range(n):
        for j in range(n):

            ten_cnt = A[i][j]
            x_cnt = A[i][j]
            distance = 1
            while True:
                for k in range(0,4):
                    if 0 <= i+di[k]*distance < n and 0 <= j+dj[k]*distance < n:
                        ten_cnt += A[i+di[k]*distance][j+dj[k]*distance]
                        # print(f"ten {ten_cnt}")
                for k in range(4, 8):
                    if 0 <= i + di[k] * distance < n and 0 <= j + dj[k] * distance < n:
                        x_cnt += A[i+di[k]*distance][j+dj[k]*distance]
                        # print(f"x {x_cnt}")
                distance += 1

                if distance == m:
                    break
            if max(ten_cnt, x_cnt) > max_fly:

                max_fly = max(ten_cnt, x_cnt)
                # print(max_fly, i, j)
    print(f"#{tc} {max_fly}")
