def perm(i, selected, j_list):
    global cnt
    global now_sum
    global min_sum
    # 가지치기를 앞에 위치시켜야 편함.
    if now_sum > min_sum:
        return
    if i == n:
        cnt += 1

        if now_sum < min_sum:
            min_sum = now_sum




    for j in range(n):

        if j not in j_list:

            selected[i] = Arr[i][j]
            j_list[i] = j
            if i == 0:
                now_sum = 0
            now_sum += Arr[i][j]

            perm(i+1, selected, j_list)
            selected[i] = 0
            j_list[i] = ""
            now_sum -= Arr[i][j]
    return min_sum


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    p_list = [0] * n
    j_list = [""] * n

    Arr = [0]* n
    cnt = 0
    now_sum = 0
    min_sum = 1000
    for i in range(n):
        Arr[i] = list(map(int, input().split()))





    print(f"#{tc} {perm(0, p_list, j_list)}")