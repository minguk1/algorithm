#G 그래프 정보
#v 시작 정점 번호
#n 정점 개수

def bfs(G, v, n):
    #방문 배열
    visited = [0] * (n+1)
    q = []
    q.append(v)
    visited[v] = 1
    while q:
        t = q.pop(0)
        print(t)
        print(node[t])
        print(visited)

        for i in G[t]: #인접 리스트 중
            if not visited[i]:
                q.append(i)
                visited[i] = visited[t] + 1






    pass
#        0    1    2    3    4    5    6    7    8    9
node = ['x', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
'''
1. 그래프의 정보가 주어지는데 어떻게 처리할거냐
정점의 개수 V
V = 9
간선의 개수 E
E = 8
9 8
1 2
1 3
1 4
2 5
2 6
4 7
4 8
4 9

'''
'''
V = 7
E = 8
7 8
1 2
1 3
2 4
2 5
3 7
4 6
5 6
6 7
'''
V, E = map(int, input().split())
G = [[] for _ in range(V + 1)]

for i in range(E):
    start, to = map(int, input().split())
    G[start].append(to)
    G[to].append(start)

bfs(G, 1, 9)
print(G)