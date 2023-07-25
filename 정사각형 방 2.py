T = int(input())
for tc in range(1, T+1):
    n = int(input())
    Arr = [0]*n
    for i in range(n):
        Arr[i] = list(map(int, input().split()))
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    visit_list = [[0]*n for _ in range(n)]

    max_value = 0
    max_list = []
    for l in range(n):
        for m in range(n):
            i = l
            j = m
            if not visit_list[i][j]:
                cnt = 1
                repeat = False
                while repeat == False:

                    visit_list[i][j] = 1
                    # print(i, j)
                    for k in range(4):
                        ni = i + di[k]
                        nj = j + dj[k]
                        if 0 <= ni < n and 0 <= nj < n and Arr[ni][nj] - 1 == Arr[i][j]:
                            i, j = ni, nj
                            cnt += 1
                            break
                    else:
                        repeat = True




                if cnt >= max_value:
                    max_value = cnt
                    max_list.append([Arr[l][m], max_value])
    # print(max_list)
    # print(max_value)
    min_num = n**2
        # print(max_list[0][0])
        # print(type(max_list[0][1]))

    for i in range(len(max_list)):
        if max_list[i][1] == max_value:

            if max_list[i][0] < min_num:
                min_num = max_list[i][0]
    print(f"#{tc} {min_num} {max_value}")