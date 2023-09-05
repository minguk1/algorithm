
def solution(n, computers):
    # 부모를 나타내기 위해 점 개수에 해당하는 리스트 생성
    parent = [i for i in range(n)]
    # 연결된 줄기가 많은 뿌리에 연결해주기 위해 그 수를 나타내려고 개수 리스트 생성
    rank = [0] * n

    # 부모 찾기 함수
    def find(parent, x):
        # 해당 점 자체가 부모가 될 때까지 계속 재귀 반복
        if parent[x] == x:
            return x

        # 위에 종료 조건이 되어 find 안에 값이 나온다면 다시 돌아오면서 싹다 한 뿌리로 직접 연결
        parent[x] = find(parent, parent[x])
        return parent[x]

    # 뿌리 합치기
    def union(parent, x, y, rank):
        # 각각 x와 y의 뿌리를 찾기
        rootX = find(parent, x)
        rootY = find(parent, y)
        # 그 뿌리가 같다면 굳이 뭘 더 안해줘도 된다.
        if rootX == rootY:
            return
        # y의 뿌리가 줄기가 더 많다면 x가 밑으로 들어간다.
        if rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
            # y의 줄기 1 더해준다.
            rank[rootY] += 1
        # x의 뿌리가 더 많거나 같다면
        else:
            # y가 x 밑으로 들어온다.
            parent[rootY] = rootX
            rank[rootX] += 1


    for i in range(n):
        # 대칭 행렬이니 대각선 오른쪽 윗부분만 돌아줘도 충분히 연결이 다 된다.
        for j in range( i +1, n):
            # 1이라면 연결이 되었단 뜻이니
            if i != j and computers[i][j] == 1:
                # 각각의 뿌리 연결
                union(parent, i, j, rank)

    print(parent)
    print(len(set(parent)))
    # 가장 중요한 것은 모두 합치고 나면 부모가 살짝씩 변화가 있을 수 있어
    # 다시 전체적으로 부모 찾기 한번씩 들어가야 한다. 명심!
    new = set()
    for i in range(n):
        new.add(find(parent, parent[i]))
    # 그 세트의 개수가 뿌리(네트워크)의 개수이다.
    answer = len(set(new))
    return answer