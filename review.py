T = int(input())

for i in range(1,T+1):
    a = list(map(int, input().split()))
    for j in range(0,9):
        total = 0
        if a[j] % 2 == 0:
            total = total
        else:
            total += a[j]
    print(f"#{T} {total}")