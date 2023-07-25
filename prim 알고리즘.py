'''
6 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''

# s : 시작 정점
# V : 정점 개수

def prim(s, V):
    MST = [0] * (V+1) # MST 포함 여부를 통해 사이클이 형성되지 않도록 설정하는듯?
    MST[s] = 1
    # 최소 신장트리 가중치 합 설정
    maxv = 0
    # 우리가 V개의 정점을 연결할 것
    for _ in range(V):
        # u는 아직 정해져있지 않다
        # u는 어떤 i랑 연결된 j 중에 최소 가중치를 가진 정점
        u = 0
        minV = 10000 # 연결된 정점 중 최소 가중치를 찾을 것

        # MST에 포함된 정점 i와 인접한 정점 j 중에서 MST에 포함되지 않고
        # 가중치가 최소인 정점 u를 찾기

        for i in range(V+1):
            # MST에 포함되어 있는 i라면
            if MST[i] == 1:
                for j in range(V+1):
                    # i와 j가 인접 정점이고 j가 MST에 포함되지 않고 그 값이 최소 가중치보다 작다.
                    if adjm[i][j] > 0 and MST[j] == 0 and minV > adjm[i][j]:
                        u = j
                        minV = adjm[i][j]

        maxv += minV
        MST[u] = 1
    return maxv



V, E = map(int,input().split())
adjm = [[0]*(V+1) for _ in range(V+1)]

for _ in range(E):
    s, e, w = map(int, input().split())
    adjm[s][e] = w
    adjm[e][s] = w

print(prim(0, V))