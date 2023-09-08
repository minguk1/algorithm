T = int(input())
for tc in range(1, T+1):

    V, E = map(int, input().split())

    adjm = [[0]*(V+1) for _ in range(V+1)]
    
    for _ in range(E):
        s, e, w = map(int, input().split())
        adjm[s][e] = w
        adjm[e][s] = w

    def prim(s, V):
        MST = [0] * (V+1)
        MST[s] = 1
        total = 0
        for _ in range(V):

            u = 0
            minV = 20000

            for i in range(V+1):

                if MST[i] == 1:
                    for j in range(V+1):
                        if adjm[i][j] > 0 and MST[j] == 0 and adjm[i][j] < minV:
                            minV = adjm[i][j]
                            u = j


            total += minV
            MST[u] = 1

        return total

    print(f"#{tc} {prim(0, V)}")