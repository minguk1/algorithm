di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]

def search(i,j,k):
    global cnt
    global success
    ni = i + di[k]
    nj = j + dj[k]

    if 0 <= ni < n and 0 <= nj < n and Arr[ni][nj] == "o":
        cnt += 1
        # print(cnt, i, j, ni, nj)
        if cnt == 4:
            success = True
            return
        search(ni, nj, k)
    else:
        cnt = 0
        return
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    Arr = [""]*n
    for i in range(n):
        Arr[i] = list(input())
    success = False
    for i in range(n):
        for j in range(n):
            if Arr[i][j] == "o":

                for k in range(8):
                    search(i, j, k)
                    if success == True:
                        break
            if success == True:
                break
        if success == True:
            break

    if success == True:
        print(f"#{tc} YES")
    else:
        print(f"#{tc} NO")