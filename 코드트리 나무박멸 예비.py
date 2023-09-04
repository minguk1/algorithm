n, m, kk, c = map(int, input().split())
ground = [0] * n

for i in range(n):
    ground[i] = list(map(int, input().split()))

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
ki = [-1, -1, 1, 1]
kj = [-1, 1, 1, -1]

# 주변의 나무 개수 세기
def around_tree(i, j):
    tree_count = 0
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]

        if 0 <= ni < n and 0 <= nj < n and ground[ni][nj] > 0:
            tree_count += 1
    return tree_count

# 주변에 나무가 뻗어 나갈 수 있는 개수 세기
def around_zero(i, j):
    zero_count = 0
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]

        if 0 <= ni < n and 0 <= nj < n and ground[ni][nj] == 0:
            zero_count += 1
    return zero_count

# 제초할 개수 구하기
def kill_tree(i,j,kk):
    # 나무가 있는 경우
    kill_sum = 0
    if ground[i][j] > 0:
        kill_sum = ground[i][j]

        for k in range(4):
            t = 0
            while True:
                ni = i + ki[k]*(t+1)
                nj = j + kj[k]*(t+1)

                if 0 <= ni < n and 0 <= nj < n and ground[ni][nj] <= 0:
                    break
                if 0 <= ni < n and 0 <= nj < n and ground[ni][nj] == -1:
                    break
                if 0 <= ni < n and 0 <= nj < n and ground[ni][nj] > 0:
                    kill_sum += ground[ni][nj]

                t += 1
                if t == kk:
                    break
        return kill_sum
    # 나무가 없는 경우
    else:
        return 0

mm = 0
kill_sum_tree = 0

while True:

    # 나무 수 늘리기
    for i in range(n):
        for j in range(n):
            if ground[i][j] > 0:
                ground[i][j] += around_tree(i, j)

    # 번식만을 위한 예비 행렬 구하기
    plus_tree = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            div_tree = 0
            if ground[i][j] > 0 and around_zero(i, j) > 0:

                div_tree = ground[i][j] // around_zero(i,j)
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if 0 <= ni < n and 0 <= nj < n and ground[ni][nj] == 0:
                        plus_tree[ni][nj] += div_tree

    for i in range(n):
        for j in range(n):
            ground[i][j] += plus_tree[i][j]

    # 최대 박멸 위치와 죽이는 나무 수 구하기
    kill_max = 0
    s, t = 0, 0
    for i in range(n):
        for j in range(n):
            if kill_tree(i,j,kk) > kill_max:
                kill_max = kill_tree(i,j,kk)

                s, t = i, j

    # 죽이는 나무 수가 0이라면 계속 진행해봤자 같을 것이다.
    if kill_max == 0:
        break
    # 좀따 최종 죽여야하는 나무 수에 더해주기
    kill_sum_tree += kill_max

    # 나무 죽이기
    ground[s][t] = (-2)*(c+1)
    for k in range(4):
        pp = 0
        while True:
            ni = s + ki[k] * (pp + 1)
            nj = t + kj[k] * (pp + 1)

            if 0 <= ni < n and 0 <= nj < n and ground[ni][nj] == -1:
                break
            if 0 <= ni < n and 0 <= nj < n and ground[ni][nj] <= 0:
                ground[ni][nj] = (-2)*(c+1)
                break
            if 0 <= ni < n and 0 <= nj < n and ground[ni][nj] > 0:
                ground[ni][nj] = (-2)*(c+1)
                # print(pp, ni, nj)
            pp += 1
            if pp == kk:
                break

    # 제초제 카운트 빼기
    for i in range(n):
        for j in range(n):
            if ground[i][j] < 0 and abs(ground[i][j]) % 2 == 0:

                ground[i][j] += 2


    mm += 1
    if mm == m:
        break

print(kill_sum_tree)