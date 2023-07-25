T = int(input())
for tc in range(1, T+1):

    n = int(input())
    food = [0] * n

    for i in range(n):
        food[i] = list(map(int, input().split()))
    # print(food)
    min_dif = 99999999

    def cook(i, A, B):
        global min_dif
        # print(i, A, B)
        # 종료 조건
        if len(A) == n//2:
            # print("A")
            # print(A, B)
            B = B + [j for j in range(i, n)]
            # print(A, B)
            a, b = 0, 0
            for s in A:
                for j in A:
                    a += food[s][j]


            for s in B:
                for j in B:
                    b += food[s][j]

            # print(a, b)
            if abs(a - b) < min_dif:
                min_dif = abs(a - b)
            # print("end")
            return

        if len(B) == n//2:
            # print("B")
            # print(A, B)
            A = A + [j for j in range(i, n)]
            # print(A, B)
            a, b = 0, 0
            for s in A:
                for j in A:
                    a += food[s][j]

            for s in B:
                for j in B:
                    b += food[s][j]

            # print(a,b)
            if abs(a - b) < min_dif:
                min_dif = abs(a - b)
            # print("end")
            return

        if i == n:
            # print("N")
            # print(A, B)
            a, b = 0, 0
            for s in A:
                for j in A:
                    a += food[s][j]

            for s in B:
                for j in B:
                    b += food[s][j]

            # print(a, b)
            if abs(a-b) < min_dif:
                min_dif = abs(a-b)
            # print("end")
            return




        cook(i+1, A+[i], B)
        cook(i+1, A, B+[i])



    cook(0, [], [])
    print(f"#{tc} {min_dif}")
