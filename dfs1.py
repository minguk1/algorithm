def dfs(s, V):
    #초기화
    visited = [0] * (V+1)
    stack = []

    #현재 방문한 정점을 i라고 하면
    i = s
    visited[i] = 1
    print(node[i])

    while True:
        #현재 정점 i에서 탐색할 수 있는 다음 정점 w에 대해서 w로 가는 길이 있고, w를 방문한 적이 없다면 w를 방문
        for w in range(1, V+1):
            if adj[i][w] == 1 and visited[w] == 0:
                #w로 가는 길이 있으니 현재 위치 i를 스택에 저장
                stack.append(i)
                #현재 위치 i를 다음 위치 w로 변경
                i = w
                print(node[i])
                visited[w] = 1
                #현재 위치 i에서 다른 경로를 더 확인할 필요가 없음
                break
        else:
                #더 이상 탐색할 정점이 없다면
                #내가 최근에 방문했던 정점을 스택에 넣어 놓았음
                #하나 꺼내서 그 위치로 돌아간다.
            if stack: #스택이 비어있지 않다면
                i = stack.pop()
            else: #스택이 비어있다면
                break
    return


 #인접 행렬
       # x A B C D E F G

node = ["x", "A", "B", "C", "D", "E", "F", "G"]
#0으로 채워주는 이유는 대부분 정점 문제는 1번째 부터 시작하기 때문에 인덱스 맞춰주기위해
#ex) 1번째 정점은 A이다. A인덱스를 1로 맞춰주기 위해
adj =  [[0,0,0,0,0,0,0,0], #x
        [0,0,1,1,0,0,0,0], #A
        [0,1,0,0,1,1,0,0], #B
        [0,1,0,0,0,1,0,0], #C
        [0,0,1,0,0,0,1,0], #D
        [0,0,1,1,0,0,1,0], #E
        [0,0,0,0,1,1,0,1], #F
        [0,0,0,0,0,0,1,0]] #G
dfs(1, 7)

'''
V , E = map(int, input().split())
adj = [[0]*(V+1) for _ in range(V+1)]
for i in range(E):
    start, end = map(int, input().split())
    adj[start][end] = 1
    adj[end][start] = 1
'''
#인접 리스트
#adj_list[i] -- i번 접점에 연결되어 있는 접점들의 리스트
'''
for i in range(E):
    start, end = map(int, input().split()) 
    adj_list[start].append(end)             
    adj_list[end].append(start)
'''