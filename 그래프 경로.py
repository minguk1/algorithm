def dfs(a,b,c):

    i = a
    visit = [0] * (b + 1)
    stack = []
    visit[i] = 1
    # print(i, end="")

    while True:
        for w in range(1, b + 1):
            # print(w)
            if arr[i][w] == 1 and visit[w] == 0:
                stack.append(i)
                i = w
                # print(f"-{i}", end="")
                visit[w] = 1
                break
        else:
             if stack:
                 i = stack.pop()

             else:
                break
        if i == c:
            visit[c] = 1
            break
    return visit
T = int(input())
for tc in range(1, T+1):
    v, e = map(int, input().split())
    arr = [[0]*(v+1) for _ in range(v+1)]
    for i in range(e):
        st, en = map(int, input().split())
        arr[st][en] = 1
    # print(arr)
    a, b = map(int, input().split())
    dfs(a,v,b)
    # print(dfs(a, v, b))
    if dfs(a,v,b)[b] == 1:
        print(f"#{tc} 1")
    else:
        print(f"#{tc} 0")