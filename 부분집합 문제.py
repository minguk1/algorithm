T = int(input())
for ts in range(1, T+1):

    N, K = map(int, input().split())
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    n = len(A)
    result_num = 0
    for i in range(1<<n):
        sub_set = []
        for j in range(n):
            if i & (1<<j):
                # print(A[j], end=" ")
                sub_set.append(A[j])
        if len(sub_set) == N and sum(sub_set) == K:
            print(sub_set)
            result_num += 1
    print(f"#{ts} {result_num}")

# A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# n = len(A)
# result_num = 0
# for i in range(1<<n):
#     sub_set = []
#     for j in range(n):
#         if i & (1<<j):
#             print(A[j], end=" ")
#             sub_set.append(A[j])
