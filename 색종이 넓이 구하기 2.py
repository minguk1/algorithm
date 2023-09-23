T = int(input())
paper_space = [[0]*100 for i in range(100)] #도화지의 공간 표현


for i in range(T):
    a, b = map(int, input().split()) #x좌표와 y좌표를 a와 b로 입력 받기
    for x in range(a, a+10):
        for y in range(b, b+10):
            paper_space[x][y] += 1 #입력받은 x, y좌표를 기준으로 + 10 의 영역까지 1씩 더해주기

#색종이가 놓여진 공간에는 0이 1이상의 수로 바뀌기 때문에 0의 개수(면적)를 세어 전체 도화지 면적에서 빼준다.
count = 0
for i in range(0, 100):
    count = count + paper_space[i].count(0)


width = 10000 - count #최종 색종이 면적
print(width)