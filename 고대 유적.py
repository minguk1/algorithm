def count(arr):
    mx = 2
    for lst in arr:
        cnt = 0
        for i in lst:
            if i == 1:
                cnt += 1
                if mx < cnt:
                    mx = cnt
            else:
                cnt = 0
    return mx

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr_t = list(map(list, zip(*arr)))

    ans = count(arr)
    ans_t = count(arr_t)

    print(f"#{tc} {max(ans, ans_t)}")