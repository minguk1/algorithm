Arr = [[0]*10 for _ in range(10)] #테스트 케이스를 반복해도 기본 행렬은 그대로이므로 미리 만들어줍니다.

T = int(input())
for tc in range(1, T+1): #입력 받은 테스트 케이스만큼 반복
    N = int(input()) #두더지 개수 입력
    r, c = map(int, input().split()) #현재 망치 좌표 입력
    doduji = [] #두더지 정보들을 모으기 위해 빈 리스트 생성
    for i in range(N):
        doduji.append(list(map(int, input().split())))
        # [두더지 행, 두더지 열, 머무는 시간] 순으로 리스트에 저장합니다.
    i = 0
    #i번째 두더지부터 시작
    cnt = 0
    #잡은 횟수를 세어주기 위해 미리 카운트 만들어줍니다.
    while True:
        x = abs(r-doduji[i][0]) #세로
        #계산의 편리성을 위해 세로 길이 차를 하나의 변수로 만들어줍니다

        y = abs(c - doduji[i][1]) #가로
        #가로축 또한 만들어 줍니다.

        if x+y <= doduji[i][2]: #K보다 가로 세로 길이 합이 더 작거나 같을 경우 무조건 두더지를 잡습니다.
            #그리고 두더지를 잡자마자 그 위치가 망치의 다음 좌표가 됩니다.
            cnt += 1
            r = doduji[i][0]
            c = doduji[i][1]

            i += 1
        else: #K가 길이 합보다 작아 두더지를 못잡는 경우입니다.
            if y >= doduji[i][2]: #가로 길이부터 움직이는데, 가로 길이 자체가 K보다 클 경우 가로만 움직이고 세로는 그대로 입니다.

                if c >=  doduji[i][1]: #망치가 두더지보다 오른쪽에 있는 경우
                    c = c - doduji[i][2]

                else: #망치가 두더지보다 왼쪽에 있는 경우
                    c = c + doduji[i][2]


            else: #K가 가로 길이보다 크지만 가로 세로의 합보다 작을 경우 가로는 두더지랑 좌표가 같아지지만 세로는 가는 도중에 두더지가 들어갑니다.
                c = doduji[i][1] # 망치의 가로 좌표가 두더지의 가로 좌표가 됩니다.
                if r >= doduji[i][0]: #망치가 두더지보다 위에 있을 경우
                    r = r - (doduji[i][2] - y) #K초 동안 가로 움직이고 나머지 시간만큼 이동할 수 있습니다.

                else:
                    r = r + (doduji[i][2] - y)

            cnt = cnt #두더지를 못잡았으니 잡은 횟수는 그대로
            i += 1 #다음 두더지로 넘어갑니다.

        if i == N: #i가 N-1번째가 끝났을 때 반복문 종료
            break
    print(f"#{tc} {cnt}")