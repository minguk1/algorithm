T = input()
if len(T) == 1:
    T = str(0) + T

S = T

i = 0

while True:
    K = int(S[0]) + int(S[1])
    K_str = str(K)
    if len(K_str)==1:
        K_str = str(0) + K_str

    P = S[1] + K_str[1]
    i = i + 1
    if P == T:
        print(i)
        break
    else:
        S = P



