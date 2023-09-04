from collections import deque

n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]


visited = [-1] * n
q = deque()

for i in range(n):
    if visited[i] != -1:
        continue

    connect = False

    # 현재 그 전 점들에서 아무하고도 연결하지 않았다.
    # 연결 됐다면 이미 visited에 그 전 점 번호가 찍혔을 것이다.
    if visited[i] == -1:
        for j in range(n):
            # 그런 점과 연결된 점이 있다면
            if i != j and computers[i][j] == 1:
                connect = True
                break

    if connect == True:
        q.append(i)
        visited[i] = i
        while q:
            start = q.popleft()
            for j in range(n):
                if j != start:
                    if computers[start][j] == 1:
                        if visited[j] == -1:
                            visited[j] = visited[start]
                            q.append(j)
                        else:
                            visited[start] = visited[j]
    # 그런 점과 하나도 연결되지 않았다면 그거 하나 자체가 네트워크
    elif connect == False and visited[i] == -1:
        visited[i] = i
    print(i, visited)

print(visited)
print(len(set(visited)))