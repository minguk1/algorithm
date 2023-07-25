# A = [1, 2, 3, 4]
# bit = [0] * 4
# for i in range(2):
#     bit[0] = i
#     for j in range(2):
#         bit[1] = j
#         for k in range(2):
#             bit[2] = k
#             for l in range(2):
#                 bit[3] = l
#                 print(bit, end=' ')
#                 s = 0
#                 for p in range(4):
#                     if bit[p] == 1:
#                         print(A[p], end = ' ')
#                         s += A[p]
#                 print(s)
arr = [3,-2,-1,-4,5,4]
n = len(arr)
#부분집합에 포함되면 1로 표시, 포함되지 않으면 0으로 표시
#arr 자리
#[2^0 2^1 2^2 2^3 2^4 2^5]
#[1, 0, 0, 1, 1, 0] >> 0b011001 >> 1 + 8 + 16 = 25번째 부분집합
#[1, 0, 0, 0, 0, 0] >> 0b000001 >> 1 > 첫번째 부분집합
#[0, 0, 0, 0, 0, 0] >> 0 > 0번째 부분집합
for i in range(1<<n): #i번째 부분집합에 대해
    print(f"{i}번째 부분집합", end=" ")
    sub_set = []
    for j in range(n): #i번째 부분집합이 n개 원소 중에 j번째 원소를 포함하는지 검사
        if i & (1 << j): #i를 이진수로 바꿨을 때 j번째 원소가 1인 경우 그 j번째 원소를 포함하는 부분 집합
            print(arr[j], end=", ")
            sub_set.append(arr[j])
    # print(sub_set)
    # if sum(sub_set) == 0:
    #     print(f"합이 0인 부분집합 : ", sub_set)
    print()
