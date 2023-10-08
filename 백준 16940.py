from collections import deque

n = int(input())
base = [[] for _ in range(n+1)]

for i in range(n-1):
    s, e = map(int, input().split())
    base[s].append(e)

selection = list(map(int, input().split()))
visited= [0]*(n+1)
total = [1]
def bfs(s, n):
    q = deque()
    q.append(s)
    visited[s] = 1

    while q:
        p = q.popleft()
        t = []
        for to in base[p]:
            if not visited[to]:
                t.append(to)
                q.append(to)
                visited[to] = visited[p]+1
        total.append(t)

bfs(1,n)
# print(visited)
# print(selection)
print(total)
able = True

idx = 0
while True:
    if idx == 0 and selection[idx] != 1:
        able = False
        break
    if idx >= 1 and visited[selection[idx]] < visited[selection[idx-1]]:
        able = False
        break
    if visited[selection[idx]] == 0:
        able = False
        break
    idx += 1
    if idx == len(selection):
        break

print(int(able))
