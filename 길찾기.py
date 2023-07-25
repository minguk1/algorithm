T = 10
for tc in range(1, 11):

    n, m = map(int, input().split())
    arr1 = [0]*100
    arr2 = [0]*100
    input_list = list(map(int, input().split()))
    # print(input_list)
    for i in range(len(input_list)):
        if i % 2 == 0 and arr1[input_list[i]] == 0:
            arr1[input_list[i]] = input_list[i+1]
        elif i % 2 == 0:
            arr2[input_list[i]] = input_list[i+1]
            # print(i)

    # print(arr1)
    # print(arr2)

    def dfs():
        i = 0
        visit = [0] * 100
        stack = []
        visit[i] = 1
        while True:
            for w in range(1, 100):
                if (arr1[i] == w or arr2[i] == w) and visit[w] == 0:
                    stack.append(i)
                    i = w
                    visit[i] = 1
                    break
            else:
                if stack:
                    i = stack.pop()
                else:
                    break

            if i == 99:
                visit[99] = 1
                return 1

        return 0

    print(f"#{tc} {dfs()}")

