def bm_search(txt, pat):
    #txt 인덱스
    ti = 0
    #pat 인덱스
    pi = 0

    n = len(txt) #텍스트 길이
    m = len(pat) #패턴 길이

    skip = {}

    #패턴 안에 문자는 몇 칸 건너뛸지 정해준다.

    for p in pat:
        skip[p] = m - 1 - pat.rfind(p)

    #딕셔너리에 없는 경우는 패턴이 없다는 뜻이니 그냥 패턴 길이만큼 건너뛴다.

    print(skip)

    #패턴의 제일 뒤 글자부터 비교
    ti = m - 1
    while ti < n:
        pi = m - 1

        #같은 문자 나오면 계속 앞으로 이동

        #다른 문자 나오면 건너뛰기 표 참고해서 이동
        while txt[ti] == pat[pi]:
            if pi == 0: #패턴 찾은 것이다. 기준 위치인 ti 반환
                return ti
            ti -= 1
            pi -= 1

        #while 끝났으면 이 시작점에서 찾지 못한 것 > 건너뛰기 표에 있는 문자가 나오면 표에 적힌대로 skip
        #건너뛰기 표에 없으면 패턴 길이만큼 skip

        offset = skip.get(txt[ti]) if skip.get(txt[ti]) else m

        #다시 비교를 시작할 위치 정해준다.
        #위에서 계산한 건너뛰기만큼 이동

        ti += offset if offset > m - pi else m - pi

    #여기까지 오면 (반복 종료) 못 찾은 것
    return -1

t = "zzzabcdadfsdfdsffsdf"
p = "abcdad"
print(f"res : ", bm_search(t, p), t.find(p))