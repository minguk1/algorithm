T = int(input())
for tc in range(1, T+1):

    n, m = map(int, input().split())
    Arr = [[0]*(n+2) for _ in range(n+2)]
    Arr[n//2][n//2], Arr[n//2+1][n//2+1] = 2, 2
    Arr[n//2][n//2+1], Arr[n//2+1][n//2] = 1, 1
    for i in range(n+2):
        print(Arr[i])
    print()
    di = [-1, -1, 0, 1, 1, 1, 0, -1]
    dj = [0, 1, 1, 1, 0, -1, -1, -1]

    for i in range(m):
        a, b, color = map(int, input().split())
        Arr[b][a] = color
        for i in range(n + 2):
            print(Arr[i])
        print()
        for k in range(8):
            cnt = 1
            change_list= []
            if Arr[b+di[k]*cnt][a+dj[k]*cnt] == 0 or Arr[b+di[k]*cnt][a+dj[k]*cnt] == color:
                continue
            else:
                print(b + di[k] * cnt, a + dj[k] * cnt, cnt)
                while True:
                    if Arr[b + di[k] * cnt][a + dj[k] * cnt] != color and Arr[b + di[k] * cnt][a + dj[k] * cnt] != 0:
                        change_list.append([b + di[k] * cnt,a + dj[k] * cnt])
                        print(change_list)
                        cnt += 1
                    elif Arr[b + di[k] * cnt][a + dj[k] * cnt] == 0:
                        break
                    elif Arr[b + di[k] * cnt][a + dj[k] * cnt] == color:
                        for p in change_list:

                            Arr[p[0]][p[1]] = color
                        break
                for i in range(n + 2):
                    print(Arr[i])
                print()



        print(Arr)
    white = 0
    black = 0
    for i in range(n+2):
        black += Arr[i].count(1)
        white += Arr[i].count(2)
    print(f"#{tc} {black} {white}")