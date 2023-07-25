T = int(input())
for tc in range(1, T+1):

    n = int(input())
    Arr = [0]*n
    for i in range(n):
        Arr[i] = list(map(int, input().split()))
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    def findnext(i,j):
        global cnt
        cnt += 1

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < n and Arr[ni][nj] - 1 == Arr[i][j]:
                findnext(ni, nj)
        return
    max_value = 0
    max_list = []
    for i in range(n):
        for j in range(n):
            cnt = 0
            findnext(i, j)
            # print(cnt)
            if cnt >= max_value:
                max_value = cnt
                max_list.append([Arr[i][j], max_value])
    # print(max_list)
    # print(max_value)
    min_num = 1000
    # print(max_list[0][0])
    # print(type(max_list[0][1]))

    for i in range(len(max_list)):
        if max_list[i][1] == max_value:

            if max_list[i][0] < min_num:
                min_num = max_list[i][0]
    print(f"#{tc} {min_num} {max_value}")



