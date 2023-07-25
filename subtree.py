T = int(input())
for tc in range(1, T+1):


    e, n = map(int, input().split())

    con_list = list(map(int, input().split()))
    left = [0] * (e+2)
    right = [0] * (e+2)

    for i in range(e):
        if left[con_list[2*i]] == 0:
            left[con_list[2*i]] = con_list[2*i+1]

        else:
            right[con_list[2*i]] = con_list[2*i+1]

    # print(left)
    # print(right)
    cnt = 0
    def find(t):
        global cnt

        if t:
            find(left[t])
            find(right[t])
            cnt += 1
            if t == n:
                return cnt

    print(f"#{tc} {find(n)}")