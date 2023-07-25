T = int(input())
for tc in range(1, T+1):
    n = 5
    arr = [[""]*15 for _ in range(5)]
    input_list = [0]*5
    for i in range(5):
        input_list[i] = list(input())
    # arr_t = list(map(list, zip(*arr)))
    # print(input_list)
    for i in range(5):
        for j in range(len(input_list[i])):
            arr[i][j] = input_list[i][j]
    # print(arr)
    arr_t = list(map(list, zip(*arr)))
    # print(arr_t)
    print(f"#{tc} ", end="")
    for i in range(len(arr_t)):
        print(''.join(arr_t[i]) , end="")
    print()
# print(arr_t)
#Aa0aPAf985Bz1EhCz2W3D1gkD6x