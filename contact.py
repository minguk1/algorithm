T = 10
for tc in range(1, T+1):
    length, start = map(int, input().split())
    input_list = list(map(int, input().split()))
    from_list = []
    to_list = []
    for i in range(length):
        if i % 2 == 0:
            from_list.append(input_list[i])
        else:
            to_list.append(input_list[i])
    # print(from_list)
    # print(to_list)
    node = [[] for _ in range(101)]
    visit = [0] * 101
    # print(node)
    for i in range(len(from_list)):
        node[from_list[i]].append(to_list[i])
    # print(node)

    q = []
    q.append(start)
    visit[start] = 1

    while q:
        now = q.pop(0)

        for i in node[now]:
            if visit[i] == 0:
                visit[i] = visit[now] + 1
                q.append(i)

    # print(visit)
    for j in range(100, 0, -1):
        if visit[j] == max(visit):
            print(f"#{tc} {j}")
            break