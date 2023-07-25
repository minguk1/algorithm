T = int(input())
for tc in range(1, T+1):

    n, m = map(int, input().split())
    Arr = [[-1] *(m+2) for _ in range(n+2)]

    # print(Arr)
    for i in range(1, n+1):
        Arr[i][1:m+1] = list(map(int, input().split()))
    # print(Arr)

    di = [-1, -1, 0, 1, 1, 1, 0, -1]
    dj = [0, 1, 1, 1, 0, -1, -1, -1]
    able = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            # print(f"# {Arr[i][j]}")
            cnt = 0
            for k in range(8):
                if 0 <= Arr[i + di[k]][j + dj[k]] < Arr[i][j]:
                    cnt += 1
                    # print(cnt, Arr[i][j])
                if cnt >= 4:
                    able += 1
                    # print(f"able {Arr[i][j]}")
                    # print(able)
                    break
    print(f"#{tc} {able}")
