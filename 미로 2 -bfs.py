dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
T = 10
for tc in range(1, T+1):

    def is_valid(r, c):
        return 0 <= r < 100 and 0 <= c < 100

    def bfs(x, y):
        visited = [[0]*100 for _ in range(100)]

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
                return True


            #현재 위치 r, c에서 4방향 탐색
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]

                if is_valid(nr, nc) and maze[nr][nc] != 1 and not visited[nr][nc]:
                    q.append((nr, nc))
                    visited[nr][nc] = 1
        return False


    maze = [0] * 100
    t = int(input())
    for i in range(100):
        maze[i] = list(input())

    for i in range(100):
        for j in range(100):
            maze[i][j] = int(maze[i][j])


    print(f"#{tc} {int(bfs(1, 1))}")