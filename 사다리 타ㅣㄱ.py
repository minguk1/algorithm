for T in range(1):
    t = int(input())
    ladder = [0]*100

    for i in range(100):
        ladder[i] = list(map(int, input().split()))

    # print(ladder)
    #2좌표 찾기
    for i in range(100):
        if ladder[99][i] == 2:
            y = i
            print(i)
    #2좌표 = (99, b)
    #현재 위치
    x = 99
    y = y
    while True:
        if x == 0:
            result = y

            break
        else:
    #왼쪽에 1이 있을 때
            if ladder[x][y-1] == 1 and y >= 1:
                while y >= 1:
                    if ladder[x][y-1] == 1:
                        x = x
                        y = y - 1

                        if y == 0:
                            x = x - 1
                            break
                    else:
                        x = x - 1
                        y = y

                        break


            #오른쪽에 1이 있을 때
            elif y <= 98 and ladder[x][y+1] == 1:
                while y <= 98:
                    if ladder[x][y+1] == 1:

                        x = x
                        y = y + 1
                        if y == 99:
                            x = x - 1

                            break


                    else:
                        x = x - 1
                        y = y

                        break

            #둘다 없을 때
            else:
                x = x - 1
                y = y

    print(f"#{t} {result}")