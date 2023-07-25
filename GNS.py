# num_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
# A = [1,5,6,8,2,1,1,6]
# B = [0] * len(A)
# C = [0]*10
# a = ["ONE", "FIV", "SIX", "EGT", "TWO", "ONE", "ONE", "SIX"]
# b = [0] * len(a)
# c = {"ZRO": 0, "ONE": 0, "TWO": 0, "THR": 0, "FOR": 0, "FIV": 0, "SIX": 0, "SVN": 0, "EGT": 0, "NIN": 0 }
# for i in range(0, len(a)):
#     c[f"{a[i]}"] += 1
# for i in range(0, len(A)):
#     C[A[i]] += 1


# print(C)
# print(c)
# for i in range (1, len(C)):
#     C[i] += C[i-1]
# for i in range(1, len(c)):
#     c[num_list[i]] += c[num_list[i-1]]
# print(c)
# for i in range(len(B) - 1, -1, -1):  # 1 감소시켜줘야 올바른 자리에 넣을 수 있음 #범위 끝에 -1을 해야 0까지 계산 가능
#     C[A[i]] -= 1
#     B[C[A[i]]] = A[i]
# print(C)
# for i in range(len(b)-1,-1,-1):
#     c[a[i]] -= 1
#     b[c[a[i]]] = a[i]
# print(B)
# print(c)
# print(b)
# for i in range(len(b)-1, -1, -1):
#     c[f"{a[i]}"] -= 1
#     b
def alp_num_sort(a, b):
    num_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    c = {"ZRO": 0, "ONE": 0, "TWO": 0, "THR": 0, "FOR": 0, "FIV": 0, "SIX": 0, "SVN": 0, "EGT": 0, "NIN": 0 }

    for i in range(0, len(a)):
        c[f"{a[i]}"] += 1

    for i in range(1, len(c)):
        c[num_list[i]] += c[num_list[i - 1]]

    for i in range(len(b) - 1, -1, -1):
        c[a[i]] -= 1
        b[c[a[i]]] = a[i]
    print(c)
    return ' '.join(b)

T = int(input())
for ts in range(1, T+1):
    z = input()
    a = list(input().split())
    b = [0] * len(a)
    print(f"#{ts}")
    print(alp_num_sort(a, b))