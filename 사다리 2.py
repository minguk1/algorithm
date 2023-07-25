for T in range(10):
    t = int(input())
    ladder = [0]*100

    for i in range(100):
        ladder[i] = list(map(int, input().split()))

    # print(ladder)
    #출발점들 인덱스 찾기
    start_index=[]
    for i in range(100):
        if ladder[0][i] == 1:
            start_index.append(i)
            # print(i)
    # print(start_index)
    num_list = []
    for k in range(len(start_index)):
    #리스트 원소들 반복
        #현재 위치
        x = 0
        y = start_index[k]
        cnt = 0
        while True:
            if x == 99:
                result = cnt
                # print(result)
                num_list.append(result)
                break
            else:
        #왼쪽에 1이 있을 때
                if ladder[x][y-1] == 1 and y >= 1:
                    while y >= 1:
                        if ladder[x][y-1] == 1:
                            x = x
                            y = y - 1
                            cnt += 1
                            if y == 0:
                                x = x + 1
                                break
                        else:
                            x = x + 1
                            y = y

                            break


                #오른쪽에 1이 있을 때
                elif y <= 98 and ladder[x][y+1] == 1:
                    while y <= 98:
                        if ladder[x][y+1] == 1:

                            x = x
                            y = y + 1
                            cnt += 1
                            if y == 99:
                                x = x + 1

                                break


                        else:
                            x = x + 1
                            y = y

                            break

                #둘다 없을 때
                else:
                    x = x + 1
                    y = y

    # print(num_list)
    for k in range(len(num_list)-1, -1, -1):
        if num_list[k] == min(num_list):
            print(f"#{t} {start_index[k]}")