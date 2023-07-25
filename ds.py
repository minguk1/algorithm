def solution(N, stages):
    answer = []
    mx = max(stages)
    stack = [0] * (mx + 2)
    stack2 = [0] * (mx + 2)
    for i in range(len(stages)):
        stack[stages[i]] += 1


    for i in range(len(stack) - 2, -1, -1):
        stack2[i] = stack2[i + 1] + stack[i]

    fail = []
    for i in range(1, N + 1):
        fail.append(stack[i] / stack2[i])

    for j in range(N):
        mi, miidx = 20000000, 10000000
        for i in range(len(fail)):
            if mi > fail[i]:
                print(mi)
                print(i)
                mi = fail[i]
                miidx = i
                continue
        answer.append(i + 1)
        print(fail)
        fail[i] = 200001
        continue

    return answer[::-1]
arr = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(5, arr))