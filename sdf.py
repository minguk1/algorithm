T = int(input())

for num in range(T):
    mylist = []
    a = []
    t = int(input())

    for num_each in range(t):
        mylist.append(list(map(int, input().split())))

    new_list1 = [[0 for k in range(t)] for l in range(t)]
    new_list2 = [[0 for k in range(t)] for l in range(t)]
    new_list3 = [[0 for k in range(t)] for l in range(t)]

for i in range(t):
    for j in range(t):
        new_list1[j][t - 1 - i] = mylist[i][j]
        new_list2[t - 1 - i][t - 1 - j] = mylist[i][j]
        new_list3[t - 1 - j][i] = mylist[i][j]
print(f"#{num + 1}")
for ii in range(t):
    for jj in range(t):
        print(f"{new_list1[ii][jj]}", end='')
    print(" ", end='')
    for jj in range(t):
        print(f"{new_list2[ii][jj]}", end='')
    print(" ", end='')
    for jj in range(t):
        print(f"{new_list3[ii][jj]}", end='')
    print()