from collections import deque
n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]

def is_final(i, p, cmb):
    result = True
    for t in range(i + 1, p):
        if cmb[t] == "O":
            result = False
    return result


def solution(n, k, cmd):
    now = k
    cmb = ['O'] * n
    active = [_ for _ in range(n)]

    delete = deque()
    for k in cmd:
        idx = 0
        next = 0
        cnt = 0
        t = k.split()
        # print(t)
        # print(t[-1])
        if k[0] == "U":
            for i in range(len(active)):
                if active[i] == now:
                    idx = i
            next = active[idx - int(t[-1])]

            now = next
        #             while True:
        #                 now -= 1

        #                 if cmb[now] == "O":
        #                     cnt += 1
        #                 else:
        #                     pass
        #                 if cnt == int(t[-1]):
        #                     break

        elif k[0] == "D":
            for i in range(len(active)):
                if active[i] == now:
                    idx = i
            next = active[idx + int(t[-1])]

            now = next
            # while True:
            #     now += 1
            #     if cmb[now] == "O":
            #         cnt += 1
            #     else:
            #         pass
            #     if cnt == int(t[-1]):
            #         break

        elif k[0] == "C":
            cmb[now] = 'X'
            print(now)
            delete.append(now)
            for act in active:

                if now == act:
                    active.remove(act)
            # print(is_final(now,n, cmb))
            if is_final(now, n, cmb) == True:
                now -= 1
            else:
                now += 1
        else:
            p = delete.pop()
            cmb[p] = "O"
            # print(p)
            active.insert(p, p)
        print(k)
        print(cmb)
        print(active)
        print(delete)
        print(now)

    # print(cmb)
    # print(''.join(cmb))
    answer = ''.join(cmb)
    return answer

solution(n, k, cmd)
