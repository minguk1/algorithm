lst = [1, 2, 3, 4, 5]

n = 5
r = 3

# 부분집합 만들기
def comb(idx, R, selected):

    # 종료 조건
    if idx == n:
        print(selected)

        # if R == r:
        #     print(selected)
        return

    # 재귀 호출
    # 고르고 진행 하거나
    selected.append(lst[idx])
    comb(idx+1, R+1, selected)
    # 안고르고 진행 하거나
    selected.pop()
    comb(idx+1, R+1, selected)

# r개 짜리 조합 만들기
# R개 고를 때 까지 계속 선택
def comb2(idx, selected):
    # 종료 조건
    if len(selected) == r:
        print(selected)
        return

    # 재귀 호출
    for i in range(idx, n):
        comb2(i+1, selected + [lst[i]])


comb(0, 0, [])
print("======")
comb2(0, [])