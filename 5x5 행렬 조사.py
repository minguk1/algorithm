import random

from pprint import pprint

n = 5 #행
m = 5 #열
arr = [[random.randrange(1,11) for _ in range(m)] for _ in range(n)]

pprint(arr)

#절댓값 총합
abs_sum = 0

#상하좌우에 해당하는 행과 열 리스트
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#행 우선 순회
for x in range(n):
    for y in range(m):
        #현재 위치
        now = arr[x][y]
        print(f"arr[{x}][{y}] = {arr[x][y]}")
        temp_sum = 0 #현재위치 절댓값 합
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n: #유효한 칸인지 검사
                #절댓값 계산
                temp_sum += abs(arr[x][y] - arr[nx][ny])
        abs_sum += temp_sum

print(f"ans : {abs_sum}")

