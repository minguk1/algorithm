T = int(input())
for tc in range(1, T+1):

    v, e = map(int, input().split())
    connect_list = [[] for _ in range(v+1)]
    # print(connect_list)
    for i in range(e):
        start, end = map(int, input().split())
        connect_list[start].append(end)
        connect_list[end].append(start)
    first, end = map(int, input().split())

    visited = [0]*(v+1)


    q = []
    q.append(first)
    visited[first] = 1
    arrive = False
    while q:
        now = q.pop(0)
        # print(q)
        if now == end:
            arrive = True
            break
        for i in connect_list[now]:
            if visited[i] == 0:
                visited[i] = visited[now] + 1
                q.append(i)





    #     print(q)
    # print(visited)
    if arrive == True:
        print(f"#{tc} {visited[end]-1}")
    else:
        print(f"#{tc} 0")


