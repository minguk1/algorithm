'''
5 8
0 1 2
0 2 4
1 2 1
1 3 7
2 4 3
3 4 2
3 5 1
4 5 6
'''

# 적당힌 큰 값
INF = 10000

# s : 시작 정점

def dijkstra(s, V):
    U = [0] * ( V + 1)
    U[s] = 1 # 최소 비용이 결정된 정점 표시
    D[s] = 0 # 출발점 비용을 결정

    # s와 연결된 곳을 살펴보고 최소 비용 최신화
    # s와 연결된 e번 정점, 가중치 w에 대해
    for e, w in adjl[s]:
        D[e] = w
        print(D)
    # 남은 정점의 비용을 결정

    for _ in range(V):
        # 비용이 아직 결정되지 않은 t 정점을 찾자
        # 그 중에 D[t] 최소인 t를 찾고 싶다
        minV = INF
        t = 0
        # 찾으러 가면
        for i in range(V+1):
            # 최소 비용 아직 결정되지 않고 현재 최솟값보다 작다면
            if U[i] == 0 and minV > D[i]:
                minV = D[i]
                t = i
                print(t)
        # 최소인 t를 찾았다
        U[t] = 1
        print(_, t)

        # 이제 최소 정점인 t를 확정 지었으니 t에서 더 나아가 최솟값을 구해준다.
        # 이전까지 내가 알고 있던 비용과 새로 경로가 만들어 졌을 때 비용
        # 그 중에서 최솟값을 선택해서 최신화
        for e, w in adjl[t]:
            D[e] = min(D[e], D[t] + w)
            print(_,t, e, D)





V, E = map(int, input().split())
adjl = [[] for _ in range(V+1)]

for _ in range(E):
    s, e, w = map(int, input().split())

    adjl[s].append([e, w])
print(adjl)
# D[i] 는 시작정점 a에서 i까지 가는데 걸리는 최소 비용
# 연결이 만들어 질때마다 무한대에서 다른 값으로 바뀜
D = [INF] * (V+1)

# 시작정점을 0번이라고 했을 때 다른정점으로 가는 최소 비용 계산
dijkstra(0, V)
print(D)
