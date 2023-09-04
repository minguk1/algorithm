def section_sum(a, i, m):
    sum_value = 0
    for k in range(m):
        sum_value = sum_value + a[i+k]
    return sum_value

T = int(input())
for p in range(1, 1+T):
    sum_list = []
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(N-M+1):

        sum_list.append(section_sum(a,i,M))


    print(f"#{p} {max(sum_list)-min(sum_list)}")