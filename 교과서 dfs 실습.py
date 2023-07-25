n = 7
visit = [0] * (n+1)
        # 1 2 3 4 5 6 7
arr = [[0,0,0,0,0,0,0,0],
       [0,0,1,1,0,0,0,0],
       [0,1,0,0,1,1,0,0],
       [0,1,0,0,0,0,0,1],
       [0,0,1,0,0,0,1,0],
       [0,0,1,0,0,0,1,0],
       [0,0,0,0,1,1,0,1],
       [0,0,0,1,0,0,1,0],
       ]


def dfs(a,b):

    i = a
    visit = [0] * (b + 1)
    stack = []
    visit[i] = 1
    print(i, end="")

    while True:
        for w in range(1, b+ 1):
            if arr[i][w] == 1 and visit[w] == 0:
                stack.append(i)
                i = w
                print(f"-{i}", end="")
                visit[w] = 1
                break
        else:
             if stack:
                 i = stack.pop()

             else:
                break
    return

dfs(1, 7)


