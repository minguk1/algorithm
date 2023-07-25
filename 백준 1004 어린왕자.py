T = int(input())
for k in range(T):
    x1, y1, x2, y2 = map(int, input().split()) #출발점과 도착점의 x,y좌표를 각각 받습니다.

    k = int(input()) #행성계의 개수
    circle_list = [] #행성계 중점 좌표와 반지름에 관한 리스트 #[x, y, r]
    for i in range(k):
        circle_list.append(list(map(int,input().split())))
    # print(circle_list) #리스트 잘 만들어졌는지 확인
    count = 0
    for p in range(k):
        #두 개 다 안에 있어 통과하지 않아도 되는 경우 # 2번 조건과 3번 조건 and로 묶었습니다.
        if ((x1-circle_list[p][0])**2+(y1-circle_list[p][1])**2)**0.5 < circle_list[p][2] and ((x2 - circle_list[p][0]) ** 2 + (y2 - circle_list[p][1]) ** 2) ** 0.5 < circle_list[p][2]:
            pass
        #출발점이 해당 행성계 안에 들어있는 경우 1번 통과
        elif ((x1-circle_list[p][0])**2+(y1-circle_list[p][1])**2)**0.5 < circle_list[p][2]:
            count += 1
        #도착점이 행성계 안에 들어있는 경우 1번 통과
        elif ((x2 - circle_list[p][0]) ** 2 + (y2 - circle_list[p][1]) ** 2) ** 0.5 < circle_list[p][2]:
            count += 1
        #전부 다 행성계 밖에 있는 경우
        else:
            pass

    print(count) #통과한 횟수 출력