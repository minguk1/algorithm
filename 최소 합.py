T = int(input())
for tc in range(1, T+1):


    n = int(input())

    board = [0] * n
    for i in range(n):
        board[i] = list(map(int, input().split()))

    di = [1, 0]
    dj = [0, 1]

    sum = board[0][0]
    sum_list = []
    def move(i, j, cnt):


        global sum
        # print(i, j, cnt, sum)

        ni = i + di[0]
        nj = j + dj[0]
        mi = i + di[1]
        mj = j + dj[1]

        if cnt == 2*(n-1):
            sum_list.append(sum)
            # print(sum_list)
            return



        else:
            if 0 <= ni < n and 0 <= nj < n:
                sum += board[ni][nj]
                move(ni, nj, cnt+1)
                sum -= board[ni][nj]
            if 0 <= mi < n and 0 <= mj < n:
                sum += board[mi][mj]
                move(mi, mj, cnt+1)
                sum -= board[mi][mj]

    move(0, 0, 0)
    # print(sum_list)
    print(f"#{tc} {min(sum_list)}")
