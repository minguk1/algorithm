def solution(N, stages):
    answer = [0] * N
    cnt = [0] * (N+1)
    for i in stages:
        if i == N+1:
            continue
        else:
            cnt[i] += 1
    # print(cnt)
    dict = {}
    participant = len(stages)
    for i in range(1, N+1):
        participant -= cnt[i-1]
        dict[i] = cnt[i] / participant
    # print(dict)
    result = sorted(dict.items(), key=lambda x:x[1], reverse=True)
    print(result)
    print([result])
    for j in range(N):
        answer[j] = result[j][0]
    # print(answer)
    return answer


N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
solution(N, stages)

# print(solution(N, stages))