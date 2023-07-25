T = int(input())
for tc in range(1, T+1):

    n = int(input())

    board = [0] * n
    for i in range(n):
        board[i] = list(map(int, input().split()))

    # print(board)
    sum = 0
    visit = [0]*n
    sum_list = []

    def golf(i, cnt):
        global sum

        if cnt == n :
            # print(sum)
            sum_list.append(sum)

        else:
            if cnt == n - 1:
                sum += board[i][0]
                # print(sum, "last")
                golf(0, cnt+1)
                sum -= board[i][0]
            else:
                for j in range(n):
                    if j != i and j != 0 and visit[j] == 0:
                        sum += board[i][j]
                        visit[j] = 1
                        # print(i, j, sum, visit)
                        golf(j, cnt+1)
                        sum -= board[i][j]
                        visit[j] = 0

    golf(0, 0)
    # print(sum_list)
    print(f"#{tc} {min(sum_list)}")