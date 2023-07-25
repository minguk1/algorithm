T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnts = [0]*200
    for _ in range(N):
        s, e = map(int, input(). split())
        if s > e:
            s,e = e, x
        for i in range((s-1)//2, (e-1)//2+1):
            cnts[i] += 1
    ans = max(cnts)
    print(ans)