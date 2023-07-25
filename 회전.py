T = int(input())
for tc in range(1,T+1):

    n, m = map(int, input().split())
    idx = m % n
    input_list = list(map(int, input().split()))
    print(f"#{tc} {input_list[idx]}")