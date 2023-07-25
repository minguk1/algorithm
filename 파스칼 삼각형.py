T = int(input())
for tc in range(1, T+1):
    n = int(input())
    if n == 1:
        A = [1]

    else:
        A = [0]*n
        A[0] = [1]
        A[1] = [1, 1]
        for i in range(2, n):
            A[i] = [1]

            for j in range(1, i):

                A[i].append(A[i-1][j-1] + A[i-1][j])

            A[i].append(1)
    print(f"#{tc}")
    for i in range(n):
        for j in range(i+1):
            print(A[i][j], end=" ")
        print()
