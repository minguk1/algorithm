dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
T = 10
for tc in range(1, T+1):

    def is_valid(r, c):
        return 0 <= r < 16 and 0 <= c < 16

    def bfs(x, y):
        visited = [[0]*16 for _ in range(16)]

        q = []
        q.append((x, y))
        visited[x][y] = 1

        while q:
            r, c = q.pop(0)

            if maze[r][c] == 3:

                return True

            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]

                if is_valid(nr, nc) and maze[nr][nc] != 1 and not visited[nr][nc]:
                    q.append((nr, nc))
                    visited[nr][nc] = 1
        return False


    maze = [0] * 16
    t = int(input())
    for i in range(16):
        maze[i] = list(input())

    for i in range(16):
        for j in range(16):
            maze[i][j] = int(maze[i][j])


    print(f"#{tc} {int(bfs(1, 1))}")