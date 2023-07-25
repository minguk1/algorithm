from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


m, n = map(int, input().split())

farm = [0] * n
zero = 0
for i in range(n):
    farm[i] = list(map(int, input().split()))
    zero += farm[i].count(0)
# print(farm)
# print(zero)
visit = [[0] * m for _ in range(n)]
one_list = deque()
for i in range(n):
    for j in range(m):
        if farm[i][j] == 1:
            one_list.append([i, j])
            visit[i][j] = 1
result = True
#애초에 토마토가 전부 익지 못하는 경우
# for i in range(n):
#     for j in range(m):
#         around = 0
#         if farm[i][j] == 0:
#             for k in range(4):
#                 ni = i + di[k]
#                 nj = j + dj[k]
#                 if (ni < 0 or nj < 0) or (ni > n or nj > m):
#                     around += 1
#                 elif 0 <= ni < n and 0 <= nj < m and farm[ni][nj] == -1:
#                     around += 1
#             if around == 4:
#                 result = False
#                 # print([i, j])
#                 break
#     if around == 4:
#         break

# print(result)

#토마토가 전부 익을 수 있는 경우
#while문으로 카운트 세주면서 주변값들 1로 바꾸고 zero 개수 빼서 zero 개수 0이 될때 카운트 출력

# if result == True:
final = 0
while one_list:
    now = one_list.popleft()
    for k in range(4):
        ni = now[0] + di[k]
        nj = now[1] + dj[k]
        if 0 <= ni < n and 0 <= nj < m and visit[ni][nj] == 0 and farm[ni][nj] == 0:
            one_list.append([ni, nj])
            visit[ni][nj] = visit[now[0]][now[1]] + 1
            final = visit[ni][nj] -1
    #         zero -= 1
    # if zero == 0:
    #     break

# for i in visit:
#     print(i)

# print(final)
# else:
#     print(-1)
for i in range(n):
    for j in range(m):
        if visit[i][j] == 0 and farm[i][j] == 0:
            result = False
if result == False:
    print(-1)
else:
    print(final)


