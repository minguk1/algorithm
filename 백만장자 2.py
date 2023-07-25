T = int(input())
for tc in range(1, T + 1):

    n=int(input())
    price=list(map(int,input().split()))
    max_value = 0
    result=0
    sum = 0
    for i in range(len(price)-1,-1,-1):

        if price[i]>max_value:
            max_value = price[i]
        else:
            sum += max_value -price[i]


    print(f"#{tc} {sum}")