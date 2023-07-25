dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
T = int(input())
for tc in range(1, T+1):

    def is_valid(r, c):
        return 0 <= r < n and 0 <= c < n

    def bfs(x, y):
        visited = [[0]*n for _ in range(n)]

        q = []
        q.append((x, y))
        visited[x][y] = 1

        while q:
            # 원소를 반환하기 전에 현재 단계에서 큐의 원소를 몇개까지 하면 되는지
            r, c = q.pop(0)

            # for i in range(n):
            #     for j in range(n):
            #         if (i, j) == (r, c):
            #             print("*", end=" ")
            #         else:
            #             print(maze[i][j], end=" ")
            #     print()
            # print("==============")

            if maze[r][c] == 3:

                # print(visited)
                # print(visited[r][c]-2)
                return (visited[r][c]-2)


            #현재 위치 r, c에서 4방향 탐색
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]

                if is_valid(nr, nc) and maze[nr][nc] != 1 and not visited[nr][nc]:
                    q.append((nr, nc))
                    visited[nr][nc] = visited[r][c] + 1
        return 0

    n = int(input())
    maze = [0] * n

    for i in range(n):
        maze[i] = list(input())

    for i in range(n):
        for j in range(n):
            maze[i][j] = int(maze[i][j])
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                now_i, now_j = i, j

    print(f"#{tc} {bfs(now_i, now_j)}")