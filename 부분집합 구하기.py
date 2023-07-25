numbers = [1,2,3,4,5]
#selected[i] == 1 : 내가 i번째 원소를 부분집합에 포함 o
#selected[i] == 0 : 내가 i번째 원소를 부분집합에 포함 x
selected = [0]*5
n = len(numbers)

# 재귀함수로 부분집합 구하기
# i번째 원소를 부분집합에 포함할지 안할지 결정

# ** 합이 x보다 작은 부분집합만 구해야 한다면
x = 6
# 가지치기 - 이미 합이 10이 돼버렸을 때 그 뒤 과정 생략

def subset(i, subsum):
    # ** 지금까지 합이 x보다 크다면 그 뒤 진행 안해도됨
    if subsum >= x:
        return

    # 1. 종료조건 : 부분집합 크기가 n이 될 때
    if i == n:
        # n개의 원소에 대해 선택을 끝냈다.
        for j in range(n):
            if selected[j]:
                print(numbers[j], end= " ")
        print()
        print("===========")
        return

    # 2. 재귀호출 : i번째를 선택하고(부분집합에 포함, subsum에 포함) 다음 i+1번째 원소를 선택하러가거나
    selected[i] = 1
    subset(i + 1, subsum + numbers[i])
    # i번째를 선택하지 않고(부분집합에 포함x) 다음 i+1번째 원소를 선택하러 가거나
    # i번째 선택 안했으면 subsum에 포함x
    selected[i] = 0
    subset(i + 1, subsum)

subset(0, 0)
