for tc in range(10):
    # n = int(input())
    arr = [list(map(int, input().split()))for _ in range(100)]

    ans = [10000, 0]

    for x in range(100):
        print(x)
        cnt = 0
        y = 99
        if arr[99][x] == 0:
            continue

        else:
            while y > 0:

                arr[y][x] = 0
                if x != 99  and arr[y][x+1] == 1:
                    x = x + 1
                    cnt += 1
                elif  x != 0 and arr[y][x-1] == 1 :
                    x = x - 1
                    cnt += 1
                else:
                    y = y - 1

            t = x
            if ans[0] > cnt:
                ans[0] = cnt
                ans[1] = t
        print(ans)
    print(ans)

    print(f'#{tc+1} {ans[1]}')