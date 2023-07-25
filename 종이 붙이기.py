

def paper(n):
    a = n // 10
    # print(a)
    if a == 1:
        return 1
    elif a == 2:
        return 3
    elif a % 2 == 1:
        return 2*(paper(n-20))+paper(n-10)

    else:
        return 2*(paper(n-20))+paper(n-10)

T = int(input())
for tc in range(1, T+1):
    n=int(input())
    print(f"#{tc} {paper(n)}")
