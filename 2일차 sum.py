for t in range(10):

    T = int(input())

    A = []
    for i in range(100):
        A.append(list(map(int, input().split())))

    sum1 = 0 #가로 합
    sum2 = 0 #세로 합
    sum3 = 0 #대각선1 합
    sum4 = 0 #대각선2 합

    for i in range(100):
        if sum(A[i]) >= sum1:
            sum1 = sum(A[i]) #가로 100줄 중 최댓값

    for i in range(100): #세로 100줄 최댓값
        i_sum = 0 #세로 합을 구하기 위해 변수 설정
        for j in range(100):
            i_sum = i_sum + A[j][i]
        if i_sum >= sum2:
            sum2 = i_sum

    for i in range(100): #오른쪽 아래로 가는 대각선 합
        sum3 = sum3 + A[i][i]

    for i in range(100): #왼쪽 아래로 가는 대각선 합
        sum4 = sum4 + A[i][99 - i]

    print(f"#{T}", max(sum1, sum2, sum3, sum4)) #구한 4가지 종류의 합 중 최댓값
