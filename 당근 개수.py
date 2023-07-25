T = int(input())
for ts in range(1, T+1):

    N = int(input())
    size_list = list(map(int,input().split()))

    count_list = []
    count = 0
    for i in range(N-1):
        if size_list[i+1] > size_list[i]:
            count = count + 1
            count_list.append(count)
        else:
            count_list.append(count)
            count = 0

    print(f"#{ts} {max(count_list)+1}")
