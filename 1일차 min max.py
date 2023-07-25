def Bubble(a, T):
    for i in range(T-1, 0 , -1):
        for j in range(i):
            if a[j] > a[j+1]:
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