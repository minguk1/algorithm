
# 버블 정렬
def Bubble(a, T):
    # i가 T-1 부터 -1씩 감소하여 0이 되기 직전까지
    for i in range(T-1, 0 , -1):
        # j를 0부터 i가 될 때까지 만큼 진행
        for j in range(i):
            # 리스트의 왼쪽 값이 오른쪽 보다 크다면
            if a[j] > a[j+1]:
                # 두 개의 위치 변경 >> 가장 큰 숫자가 가장 오른쪽으로 가게 된다.
                a[j], a[j+1] = a[j+1], a[j]

    return a




t = int(input())

for i in range(1, t+1):
    n = int(input())
    input_list = list(map(int, input().split()))
    Bubble(input_list, n)
    print(f"#{i} {input_list[-1] - input_list[0]}")

# t = int(input())
#
# for i in range(1, t+1):
#     n = int(input())
#     input_list = list(map(int, input().split()))
#     max_value = 0
#     min_value = 1000000
#     for j in range(n):
#         if input_list[j] > max_value:
#             max_value = input_list[j]
#         if input_list[j] < min_value:
#             min_value = input_list[j]
#     print(f"#{i} {max_value - min_value}")