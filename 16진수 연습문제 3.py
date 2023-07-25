def solution(n):

    l = len(n) * 4

    x = int(n, 16)
    print(x)
    #결과 문자열
    result = ""
    bin = ""
    #뒤에서 부터 7개씩 잘라서 2진수 만든뒤에 다시 10 진수로 바꾸기
    for i in range(l -1, -1, -1):
        #현재 위치 i에서 7개 잘라서 만든 이진수
        bin += "1" if x & (1<<i) else "0"
        # x의 i - j번째 비트 판별
    print(bin)
    for i in range(len(bin)-1, -1, -1):
        if bin[i] == "1":
            idx = i
            break

    while True:
        result += str(change(bin[idx-5:idx+1]))
        idx -= 6
        if idx <= 5 :
            break
    print(result[::-1])
    # for j in range(6):
    #         #음수만큼 쉬프트가 일어났다 = 자릿수가 넘어갔다
    #         if i - j < 0:
    #             break
    #         bin += "1" if x & (1 << i-j) else "0"
    #     print(bin, end=" ")
    #     dec = int(bin, 2) #2진수를 10진수로 바꾸기

    #     result += str(dec) + " "
    # print()
    # print(result)
def change(n):
    if n == "001101":
        return 0
    elif n == "010011":
        return 1
    elif n == "111011":
        return 2
    if n == "110001":
        return 3
    elif n == "100011":
        return 4
    elif n == "110111":
        return 5
    elif n == "001011":
        return 6
    elif n == "111101":
        return 7
    elif n == "011001":
        return 8
    elif n == "101111":
        return 9





solution("0DEC")
solution("0269FAC9A0")