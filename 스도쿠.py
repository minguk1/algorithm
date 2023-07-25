T = int(input())
for p in range(1,T+1): #T만큼 반복

    A = []
    for i in range(9):
        A.append(list(map(int,input().split()))) #81개의 숫자를 A 리스트 안에 담았습니다.

    def matrix_func(A, i, j): #3x3행렬의 검증을 하기 위해 따로 함수를 만들었습니다.
        a_set = set()
        for m in range(3):
            for n in range(3):
                a_set.add(A[i+m][j+n]) #3x3 행렬에서 왼쪽 위 자리 기준으로 9개의 수를 하나의 리스트로 담았습니다.
        return a_set

    answer_list = [] #세 가지 방법 중 통과하지 못한 게 있으면 0을 담기 위해 따로 정답 리스트를 만들었습니다.
    for i in range(9):
        if len(set(A[i])) != 9: #A에서 1행 리스트를 세트로 변화하여 중복값이 없으면 정상적으로 원소가 9개가 나옵니다.
            answer_list.append(0) #만약 중복이 있어 원소 수가 9가 아니라면 정답 리스트에 0을 넣습니다.
            break

        else:
            answer_list.append(1)

    for i in range(9): #세로 줄을 검사하기 위해 각 열의 원소 9개를 뽑아 리스트에 넣은 다음 1부터 9까지 다 있는지 검사했습니다.
        row_set = set()
        for j in range(9):
            row_set.add(A[j][i])
        if len(row_set) != 9:
            answer_list.append(0) #만약 중복값이 있다면 0을 정답 리스트에 넣습니다.
            break
        else:
            answer_list.append(1)

    for t in range(0, 3):
        for s in range(0, 3):
            if len(matrix_func(A, 3 * t, 3 * s)) != 9: #아까 만들어 놓은 3x3행렬을 9번 돌려 그 중에 틀린 것이 있다면 0을 넣습니다.
                answer_list.append(0)
            else:
                answer_list.append(1)

    # print(answer_list)
    if 0 in answer_list: #지금까지 만들어 놓은 정답 리스트에 0이 있다면 스도쿠가 틀려 0을 출력, 0이 없다면 정상적인 스도쿠이니 1 출력!
        print(f"#{p} 0")
    else:
        print(f"#{p} 1")

# print(set(A[0]))


# for i in range(9):
#     if len(set(A[i])) != 9:
#         print(0)
#         break
#     else:
#         print(1)
#         for i in range(9):
#             row_set = set()
#             for j in range(9):
#                 row_set.add(A[j][i])
#             if len(row_set) != 9:
#                 print(0)
#                 break
#             else:
#                 for t in range(0, 3):
#                     for s in range(0, 3):
#                         if len(matrix_func(A, 3 * t, 3 * s)) != 9:
#                             print(0)
#                             break


# for i in range(9):
#     if len(set(A[i])) != 9:
#         print(0)
#         break
#
# for i in range(9):
#     row_set = set()
#     for j in range(9):
#         row_set.add(A[j][i])
#     if len(row_set) != 9:
#         print(0)
#         break
#
# for t in range(0, 3):
#     for s in range(0, 3):
#         if len(matrix_func(A, 3 * t, 3 * s)) != 9:
#             print(0)
#             break
# print(1)
