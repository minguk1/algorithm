
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def make(i, j, k, a):
    # 종료조건
    if k == 6:

        total.append(a)
        return


    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]

        if 0 <= ni < 4 and 0 <= nj < 4:
            a += num_list[ni][nj]
            make(ni, nj, k + 1, a)
            a = a[:-1]

T = int(input())
for tc in range(1, T+1):
    num_list = [0] * 4
    for i in range(4):
        num_list[i] = list(input().split())
    total = []

    for i in range(4):
        for j in range(4):
            make(i, j, 0, num_list[i][j])


    print(total)
    print(f"#{tc} {len(set(total))}")
    # print(len(set(total)))


