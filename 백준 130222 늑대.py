wolf = list(input())
print(wolf)
cnt = len(wolf)

def decide(wolf):
    answer = 1

    if cnt%4 != 0 :
        answer = 0
        print("1")
        return answer

    if (wolf.count('w')!=(cnt//4)) or (wolf.count('o')!=(cnt//4)) or (wolf.count('l')!=(cnt//4)) or (wolf.count('f')!=(cnt//4)):
        answer = 0
        print("12")
        return answer

    i = 0
    k = 0
    if wolf[i] != 'w':
        answer = 0
        print("13")
        return answer

    jungbok = 1
    while i<cnt:
        if i > cnt:
            answer = 0
            return answer
        if wolf[i] != 'w':
            jungbok = i - k
            print(i, k)
            print(jungbok)
            print(['o']*jungbok)
            print(wolf[i:i+jungbok])
            if i+jungbok > cnt or wolf[i:i+jungbok] != ['o']*jungbok:
                answer = 0
                print("14")
                return answer

            if i+jungbok*2 > cnt or wolf[i+jungbok:i+2*jungbok] != ['l']*jungbok:
                answer = 0
                print("15")
                return answer

            if i+3*jungbok > cnt or wolf[i+2*jungbok:i+3*jungbok] != ['f']*jungbok:
                answer = 0
                print("132")
                return answer
            print(i+3*jungbok)
            if i+3*jungbok == cnt:
                answer = 1
                return answer
            if i+3*jungbok > cnt or wolf[i+3*jungbok] != 'w':
                answer = 0
                print("1234")
                return answer
            else:

                i = i + 3*jungbok
                k = i

                jungbok = 1

        else:
            i += 1



print(decide(wolf))
