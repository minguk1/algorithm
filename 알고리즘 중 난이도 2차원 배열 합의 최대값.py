for t in range(10):

    T= int(input())

    A = []
    for i in range(100):
        A.append(list(map(int, input().split())))

    sum1 = 0
    sum2 = 0
    sum3 = 0
    sum4 = 0

    for i in range(100):
        if sum(A[i]) >= sum1:
            sum1 = sum(A[i])

    for i in range(100):
        i_sum = 0
        for j in range(100):
            i_sum = i_sum + A[j][i]
        if i_sum >= sum2:
            sum2 = i_sum

    for i in range(100):
        sum3 = sum3 + A[i][i]

    for i in range(100):
        sum4 = sum4 + A[i][99-i]

    print(f"#{T}", max(sum1, sum2, sum3, sum4))



