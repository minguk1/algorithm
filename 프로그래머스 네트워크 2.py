

n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]


visited = [-1] * n
visited[0] = 0

for i in range(1, n):
    connect = False
    k = i
    for j in range(i):
        if computers[i][j] == 1:
            connect = True
            k = visited[j]
            break
    visited[i] = k



print(visited)
print(len(set(visited)))