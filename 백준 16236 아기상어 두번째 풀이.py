from collections import deque

n = int(input())
sea = [0] * n
for i in range(n):
    sea[i] = list(map(int, input().split()))
    if 9 in sea[i]:
        r, c = i, sea[i].index(9) # 처음 상어 위치
        sea[r][c] = 0

size = 2
stack = 0
time = 0
total_time = 0

di = [-1, 0, 0, 1]
dj = [0, -1, 1, 0]
# def upgrade_able(size, stack):
#     cnt = 0
#     for i in range(n):
#         for j in range(n):
#             if 1 <= sea[i][j] < size:
#                 cnt += 1
#     if cnt+stack < size:
#         return False
#     else:
#         return True
def eat_able(size):
    for i in range(n):
        for j in range(n):
            if 1 <= sea[i][j] < size:
                return True
    return False

def eat_fish(i,j,size, stack, time):

    global total_time
    # print("시작",  i, j, total_time)
    if eat_able(size) == False:
        return

    visited = [[0]*n for _ in range(n)]
    visited[i][j] = 1
    q = deque()
    q.append((i,j))
    qq = deque()

    while q:
        # qq = deque()
        r, c = q.popleft()
        # print(r,c)
        # print(r,c, visited[r][c])

        for k in range(4):
            nr = r + di[k]
            nc = c + dj[k]
            if (0<=nr<n and 0<=nc<n) and visited[nr][nc]==0 and ( 0 <= sea[nr][nc] <= size):
                qq.append((nr,nc))
                visited[nr][nc] = visited[r][c] + 1

            # print(qq)
        if len(q) == 0:
            for s in range(n):
                for t in range(n):
                    # if (s, t) in qq:
                    #     print("dsdfdsf")
                    if (s, t) in qq and 1 <= sea[s][t] < size:
                        stack += 1
                        total_time += (visited[s][t] -1)
                        sea[s][t] = 0
                        if stack == size:
                            stack = 0
                            size += 1
                            if eat_able(size) == True:
                                eat_fish(s,t,size,stack, time)
                                return
                            else:
                                return
                        else:
                            if eat_able(size) == True:
                                eat_fish(s,t,size,stack, time)
                                return
                            else:
                                return
            q = qq
            # print("q" , q)
            qq = deque()

            #     stack += 1
            #     time = visited[r][c]
            #     total_time += visited[r][c]
            #     sea[nr][nc] = 0
            #     if stack == size:
            #
            #         stack = 0
            #         size += 1
            #         print("진화", size)
            #         if eat_able(size) == True:
            #
            #             eat_fish(nr, nc, size, stack, time)
            #             return
            #         else:
            #             print(time)
            #             # print("end")
            #             return
            #     else:
            #         if eat_able(size) == True:
            #             # print("더먹기가능")
            #             # print(time, "time")
            #
            #             eat_fish(nr, nc, size, stack, time)
            #             return
            #         else:
            #
            #             # print(time)
            #             return
            # elif (0<=nr<n and 0<=nc<n) and visited[nr][nc]==0 and (sea[nr][nc] == 0 or sea[nr][nc] == size):
            #     time += 1
            #     visited[nr][nc] = visited[r][c] + 1
            #     q.append((nr, nc))
            #     print("append", nr, nc)
            #

eat_fish(r,c,2,0,0)
print(total_time)