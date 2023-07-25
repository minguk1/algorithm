T = int(input())

for tc in range(1, T+1):
    S, N = input().split()

    S = list(S)
    N = int(N)


    # def perm(idx):
    #
    #     if idx == n:
    #         print(lst)
    #         return
    #
    #     for i in range(idx, n):
    #
    #         lst[idx], lst[i] = lst[i], lst[idx]
    #         perm(idx + 1)
    #
    #         lst[idx], lst[i] = lst[i], lst[idx]



    def perm2(cnt):

        if cnt == N:

            return

        for i in range(len(S)-1):
            for j in range(i+1, len(S)):
                S[i], S[j] = S[j], S[i]
                perm2(cnt + 1)
                S[i], S[j] = S[j], S[i]

    perm2(0)