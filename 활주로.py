
# for i in a:
#     B += str(i)
#
# # print(B)
# for i in B:
#     if int(i) != max(a):
#         # print(f"{i*n}")
#
#         pass
# for b in B:
#     if int(b) != max(a):
#         if f"{b*3}" not in B:
#             print(0)
n, k = map(int, input().split())
J = []

for m in range(0, n):
    J.append(list(map(int, input().split())))
# print(J)
K = [[0] * n for i in range(n)]

for i in range(n):
    for j in range(n):
        K[i][j] = J[n - 1 - j][i]
# print(K)


def check_fly(a, k):
    B = ""  # 리스트 원소들을 문자열로 바꿔주기
    for i in a:
        B += str(i)

    for i in range(len(a)-1):
        if abs(a[i]-a[i+1]) >= 2:
            return 0
    for i in a: #리스트 원소들 중
        if i != max(a): #최댓값이 아닌 i에 대해
            if a.count(i) < k: #그 i 개수가 경사대 크기보다 작을 때
                return 0
    for i in range(len(a)-1): #낮아졌다가 올라갈 때
        if a[i] - a[i+1] > 0: #낮아졌는데
            if f"{str(a[i + 1]) * 2 * k}" != B[i + 1:i + 1 +2*k]:
                for j in range(i+1, len(a)-1): #나머지 원소들에 대해서
                    if a[j]-a[j+1] < 0: #마이너스가 존재할 때
                        return 0
    #
    #
    for b in B: #최댓값이 아닌 원소가 붙어있는데 발사대 보다 작을 때
        if int(b) != max(a):
            if f"{b*k}" not in B:
                return 0


    for b in B: #발사대 세트가 된 것들 떼내어 낮은 칸들 개수 세는데 빼주기
        if int(b) != max(a):
            for m in range(len(a), k - 1, -1):
                if f"{b * m}" in B:

                    B = B.replace(f"{b * m}", "")

    # print(B)
    for b in B:  # 최댓값이 아닌 원소가 붙어있는데 발사대 보다 작을 때
        if int(b) != max(a):
            if a[0] < a[1]:

                if f"{b * k}" not in B:
                    return 0
            if a[-1] < a[-2]:
                if f"{b * k}" not in B:
                    return 0

    return 1
count = 0
for i in range(n):
    print(J[i])
    count = count + check_fly(J[i], k)
    print(check_fly(J[i], k))
for i in range(n):
    print(K[i])
    count = count + check_fly(K[i], k)
    print(check_fly(K[i], k))
print(count)
# a =[1,1,1,2,2,2,1]
# # # [4, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 4]
# # # [4, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 4]
# print(a)
# print(check_fly(a,3))

