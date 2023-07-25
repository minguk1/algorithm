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
rep = []

def find_set(x):
    while x != rep[x]:
        x = rep[x]

    return x

def union(x, y):
    rep[find_set(y)] = find_set(x)

V, E = map(int, input().split())

edge = []

for _ in range(E):
    s, e, w = map(int, input().split())
    edge.append([w, s, e])
    # w 값으로 정렬할 것이니 앞으로 당기기
    # 자동으로 리스트 제일 앞 값으로 정렬
edge.sort()
rep = [i for i in range(V+1)]

# 내가 지금까지 선택한 간선의 개수
cnt = 0

# MST 가중치의 합
total = 0

# MST의 간선수 N = 정점수 - 1
N = V + 1

for w,s,e in edge:
    # s 집합 대표와 e 집합 대표가 달라야 사이클 형성 x
    if find_set(s) != find_set(e):
        cnt += 1
        union(s, e)
        total += w

        # MST 구성이 끝나면( 트리 선 개수가 N - 1개 될 때)
        if cnt == N - 1:
            break

print(total)