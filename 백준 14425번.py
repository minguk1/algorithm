N, M = map(int, input().split())
S = []#S문자열을 입력 받기 위해 미리 빈 리스트 생성
for i in range(N):#N번을 반복하여
    S.append(input())#문자열을 S리스트에 넣어주기

# print(S)

cnt = 0
for i in range(M): #M번 반복하여
    if input() in S: #입력받은 문자열이 S리스트에 있으면
        cnt += 1 #카운트 상승

print(cnt)