n, m, v = map(int, input().split())
node1 = [[] for i in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    node1[a].append(b)
    node1[b].append(a)

node2 = [[] for i in range(n+1)]
for i in range(n+1):
    node2[i] = sorted(node1[i])

def dfs(v, n):
    visited = [0]*(n+1)
    stack = []

    i = v
    visited[i] = 1
    print(i, end=" ")

    while True:
        for k in node2[i]:
            if not visited[k]:
                stack.append(i)
                i = k
                print(k, end=" ")
                visited[k] = 1
                break
        else:
            if stack:
                i = stack.pop()
            else:
                break
def bfs(v, n):
    visited = [0]*(n+1)
    q = []

    i = v
    visited[i] = 1
    q.append(i)

    while q:
        p = q.pop(0)
        print(p, end=" ")
        for k in node2[p]:
            if not visited[k]:
                q.append(k)
                visited[k] = 1

dfs(v, n)
print()
bfs(v, n)
print()
