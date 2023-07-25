T = int(input())
for tc in range(1, T+1): #첫 줄의 테스트 케이스 수를 입력으로 받습니다.
    N, M = map(int, input().split()) # 문제에서 주어진 대로 도화지의 크기 N과 도장 횟수 M을 변수로 받습니다.
    paper = [[0]*N for _ in range(N)] #NxN크기의 이차원 행렬 paper를 만들어 주었습니다.
    M_list = [] #그 뒤로 도장의 정보를 얻기 위해 미리 빈 리스트를 만들어 줍니다.
    for m in range(M): #도장 횟수만큼 입력받은 정보를 리스트 안에 저장합니다.
        M_list.append(list(map(int, input().split())))
    #[시작 행, 시작 열, 너비, 높이] 정보로 받습니다.
    for m in range(M): # 도장 횟수 만큼 반복
        for i in range(M_list[m][0], M_list[m][0]+M_list[m][3]): #행에 대해서 시작 행부터 너비를 더한 값까지
            for j in range(M_list[m][1], M_list[m][1]+M_list[m][2]): #열에 대해서 시작 열부터 높이를 더한 값까지
                paper[i][j] += 1 #도장이 찍힌 도화지 부분에 값을 1씩 더해주었습니다.


    cnt = 0
    for i in range(N): #NxN행렬 전체에 대해서
        for j in range(N):
            if paper[i][j] >= 1: #i행 j열 원소가 도장이 찍혔을 때
                cnt += 1 #카운트가 증가하도록 설정하였습니다.
    print(f"#{tc} {cnt}") #답 출력