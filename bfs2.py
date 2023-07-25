dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def is_valid(r, c):
    return 0 <= r < n and 0 <= c < n

def bfs(sr, sc):
    visited = [[0]*n for _ in range(n)]

    q = []
    q.append((sr, sc))
    visited[sr][sc] = 1
    day = 0
    while q:
        # 원소를 반환하기 전에 현재 단계에서 큐의 원소를 몇개까지 하면 되는지
        size = len(q)

        for _ in range(size):
            r, c = q.pop(0)

            for i in range(n):
                for j in range(n):
                    if (i, j) == (r, c):
                        print("*", end=" ")
                    else:
                        print(maze[i][j], end=" ")
                print()
            print("==============")

            if maze[r][c] == 3:
                print(f"탈출: {day}")
                print(visited)
                q = []
                break

        #현재 위치 r, c에서 4방향 탐색
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]

                if is_valid(nr, nc) and maze[nr][nc] != 1 and not visited[nr][nc]:
                    q.append((nr, nc))
                    visited[nr][nc] = visited[r][c] + 1

        day += 1
n = 7

maze = [[0,0,0,0,0,0,0],
        [0,1,1,1,1,1,0],
        [0,1,0,1,0,1,0],
        [0,0,0,0,0,1,0],
        [0,1,0,0,0,1,0],
        [0,1,0,0,0,0,1],
        [0,1,3,0,0,0,1],]

bfs(0, 0)
