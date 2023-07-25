

total = [0] * 4
for i in range(4):
    total[i] = list(input())

command = []
repeat = int(input())
for i in range(repeat):
    command.append( list(map(int, input().split())))



def watch(a):

    a = [a[-1]] + a[0:-1]
    return a

def watch_reverse(a):

    # print(a[:-1])
    # print(a[0])
    a = a[1:] + [a[0]]
    return a

# print(watch(total[0]))
# # print(total[0])
# print(watch_reverse(total[0]))

def select_direction(b):
    change_list = [0,0,0,0]

    k = b[0]-1


    change_list[k] = b[1]
    # print(change_list)
    # print(k)
    # 오른쪽 방향
    while True:
        k += 1
        # print(k)
        if k == 4:
            # print('sdf')
            break
        else:
            if total[k-1][2] == total[k][6]:
                break
            else:
                change_list[k] = change_list[k-1]*(-1)
    k = b[0] - 1
    # print(k)
    # 왼쪽 방향
    while True:
        k -= 1
        if k == -1:
            break
        else:
            if total[k][2] == total[k+1][6]:
                break
            else:
                change_list[k] = change_list[k+1]*(-1)

    # print(change_list)
    return change_list

# select_direction(command[1])
for com in command:
    t = select_direction(com)
    for i in range(4):
        if t[i] == -1:
            total[i] = watch_reverse(total[i])
        elif t[i] == 1:
            total[i] = watch(total[i])
    # print(com, total)

# print(total)
result = int(total[0][0])*1 + int(total[1][0])*2 + int(total[2][0])*4 + int(total[3][0])*8

print(result)