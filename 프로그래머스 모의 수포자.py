def solution(answers):
    answer = []
    a = [1, 2, 3, 4, 5] * (2000)
    b = [2, 1, 2, 3, 2, 4, 2, 5] * (1250)
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (1000)

    result = [0, 0, 0]
    for i in range(len(answers)):
        if answers[i] == a[i]:
            result[0] += 1
        if answers[i] == b[i]:
            result[1] += 1
        if answers[i] == c[i]:
            result[2] += 1
    print(result)
    for i in range(3):
        if result[i] == max(result):
            answer.append(i + 1)

    return answer
answers=[1,2,3,4,5]
print(solution(answers))