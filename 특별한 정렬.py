T = int(input())
for ts in range(1, T+1):

    N = int(input())
    number_list = list(map(int, input().split()))

    for i in range(5):
        max_index = 2*i
        min_index = 2*i+1
        #최댓값 먼저 넣기
        for a in range(2*i, N):
            if number_list[a] > number_list[max_index]:
                max_index = a
        # print(max_index)
        number_list[2*i], number_list[max_index] = number_list[max_index], number_list[2*i]
        # print(number_list[0])
        #최솟값 뒤에 넣기
        for b in range(2*i+1, N):
            if number_list[b] < number_list[min_index]:
                min_index = b
        # print(min_index)
        number_list[2*i+1], number_list[min_index] = number_list[min_index], number_list[2*i+1]
        # print(number_list[1])
        # print(number_list)
    print(f"#{ts}", end=" ")
    print(*number_list[0:10])
