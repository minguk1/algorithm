def hansu(x):
    str_x = str(x)
    if len(str_x) == 1 or len(str_x) == 2:
        return 1
    else:
        for i in range(len(str_x)-2):
            # print(int(str_x[i]) - int(str_x[i+1]))
            # print(int(str_x[i+1]) - int(str_x[i+2]))
            if int(str_x[i]) - int(str_x[i+1]) != int(str_x[i+1]) - int(str_x[i+2]):
                return 0
                break
            else:
                # print(i)
                # print(len(str_x)-3)
                if i == len(str_x)-3:
                    return 1
                    break



N = int(input())
count = 0
for i in range(1, N+1):
    count += hansu(i)
print(count)