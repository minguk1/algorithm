n = 10
info = [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]

max_difference = 0
final = [-1]
def solution(n, info):
    lion = [0] * 11
    # global final


    def select(i, lion, cnt):
        # 종료 조건
        global final
        global max_difference
        # print(max_difference)
        if i == 11:
            # print(n-cnt)
            if cnt < n:
                lion[10] += (n-cnt)

            peach = 0
            rion = 0
            for i in range(11):
                if info[i] >= lion[i] and info[i] > 0:
                    peach += (10 - i)
                elif info[i] < lion[i] and lion[i] > 0:
                    rion += (10 - i)

            if rion - peach > max_difference:
                max_difference = rion - peach
                final = lion.copy()
                # print(max_difference)
                # print(final, i)
            elif rion - peach == max_difference:
                for i in range(11):
                    if lion[10 - i] > final[10 - i]:
                        final = lion.copy()
                        # print(final, i)
                        break
                    elif lion[10 - i] == final[10 - i]:
                        continue
                    else:
                        break

            lion[10] -= (n-cnt)
            # print(sum(lion))
            return

        if cnt == n:
            # print(lion, i)
            # print(sum(lion))
            peach = 0
            rion = 0
            for i in range(11):
                if info[i] >= lion[i] and info[i] > 0:
                    peach += (10-i)
                elif info[i] < lion[i] and lion[i] > 0:
                    rion += (10-i)

            if rion-peach > max_difference:
                max_difference = rion-peach
                final = lion.copy()
                # print(max_difference)
                # print(final,i)
            elif rion-peach == max_difference:
                for i in range(11):
                    if lion[10-i] > final[10-i]:
                        final = lion.copy()
                        # print(final)
                        return
                    elif lion[10-i] == final[10-i]:
                        continue
                    else:
                        break
            return



        k = info[i] + 1

        # i번째 점수를 취득 할 때
        # 남은 화살이 어피치 개수 +1 보다 더 많아 더 많이 맞출 수 있을 때
        if k <= n - cnt:
            lion[i] = k
            # print('here', lion, i)
            select(i + 1, lion, cnt + k)
        # 남은 화살이 맞춰야 하는 개수 이상으로 점수를 어차피 딸 수 없을 때 넘겨야 한다.
        else:
            pass
        # i번째 점수를 포기 할 때
        lion[i] = 0
        select(i + 1, lion, cnt)

    select(0, lion, 0)
    print(final)
    answer = final
    print(answer)
    return answer

print(solution(n, info))
# solution(n, info)