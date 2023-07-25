T = int(input())

for tc in range(1, T+1):
    n = float(input())
    # 이진수로 바꾼 결과 b
    b = ""
    # 자릿수 cnt
    cnt = 0

    #반복문 돌면서 이진수로 바꾸기
    # 원래수 * 2 한 결과가 1이상이라면 이진수에 1 추가
    # 1 빼주고 다음 계산 이어나간다.
    # 원래수 * 2 한 결과가 1 미만이라면 이진수에 0 추가
    # 자릿수 13 이상이면 overflow
    # 결과가 0이면 반복 중단

    while True:
        double = 2*n
        cnt += 1
        if cnt == 13:
            b = "overflow"
            break
        if double == 1:
            b += "1"
            break
        elif double > 1:
            b += "1"
            n = double - 1
        else:
            b += "0"
            n = double

    print(f"#{tc} {b}")