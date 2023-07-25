
# T = int(input())
# for tc in range(1, T+1):
#     n = int(input())
#     A = [0]*n
#     for i in range(n):
#         A[i] = list(map(int, input()))
#     # print(A)
#     stack = []
#     visit = []
#     for i in range(n):
#         for j in range(n):
#             # print(count0(A, i, j, n))
#             if A[i][j] == 2:
#                 r, s = i, j
#                 stack.append([r, s])
#                 visit.append([r, s])
#                 # print(stack, visit)
#     di = [-1, 1, 0, 0]
#     dj = [0, 0, -1, 1]
#     result = 0
#     while result==0:
#         for k in range(4):
#             x = r + di[k]
#             y = s + dj[k]
#             if 0<=x<n and 0<=y<n and A[x][y] == 3:
#                 result = 1
#                 break
#             if 0<=x<n and 0<=y<n and A[x][y] == 0 and  [x, y] not in visit:
#                 r = x
#                 s = y
#                 # print(r,s)
#                 visit.append([r, s])
#
#
#                 stack.append([r, s])
#                 break
#         else:
#             if stack:
#                 # print(stack)
#                 # print(stack.pop())
#
#                 r = stack[-1][0]
#                 s = stack.pop()[1]
#                 # print(r,s)
#
#             else:
#
#                 break
#
#     print(f"#{tc} {result}")
# #
T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    A = [0] * n
    for i in range(n):
        A[i] = list(map(int, input()))

    # print(A)
    stack = []
    visit = []
    for i in range(n):
        for j in range(n):
            # print(count0(A, i, j, n))
            if A[i][j] == 2:
                r, s = i, j
                stack.append([r, s])
                visit.append([r, s])
                # print(stack, visit)
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    result = 0
    while result == 0:
        for k in range(4):
            x = r + di[k]
            y = s + dj[k]
            if 0 <= x < n and 0 <= y < n and A[x][y] == 3:
                result = 1
                break
            if 0 <= x < n and 0 <= y < n and A[x][y] != 1 and [x, y] not in visit:
                stack.append([r, s])
                r = x
                s = y
                # print(r,s)
                visit.append([r, s])

                break
        else:
            if stack:
                # print(stack)
                # print(stack.pop())

                r = stack[-1][0]
                s = stack.pop()[1]
                # print(r,s)

            else:

                break

    print(f"#{tc} {result}")
#
#
#

