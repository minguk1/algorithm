n = int(input())


def star(n):
    if n == 3:
        # print("***")
        # print("* *")
        # print("***")

        lst = [["*","*","*"],
               ["*"," ","*"],
               ["*","*","*"]]
        # for l in lst:
        #     print(''.join(l))

        return lst

    else:
        # star(n/3)
        # star(n/3)
        # star(n/3)
        n_list = [[" "]*n for _ in range(n)]
        m_list = star(n//3)
        # print(m_list)
        # for m in m_list:
        #     print(''.join(m))
        # print(n_list)
        # print(n_list[8][8],n_list[8])
        for i in range(3):
            for j in range(3):
                for m in range(n//3):
                    for k in range(n//3):
                        # print(i,j,m,k)
                        # print(3*i+m, 3*j+k)
                        n_list[n//3*i+m][n//3*j+k] = m_list[m][k]
                        # print(3*i+m, 3*j+k)
                        # print(n_list)
        for i in range(n):
            for j in range(n):
                if (n//3 <= i < n//3*2) and (n//3 <= j < n//3*2):
                    n_list[i][j] = " "
        # print(n_list)
        # for n in n_list:
        #     print(''.join(n))
        return(n_list)

star(n)
for n in star(n):
    print(''.join(n))