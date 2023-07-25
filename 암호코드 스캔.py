decrypt = {
    (2, 1, 1) : 0,
    (2, 2, 1) : 1,
    (1, 2, 2) : 2,
    (4, 1, 1) : 3,
    (1, 3, 2) : 4,
    (2, 3, 1) : 5,
    (1, 1, 4) : 6,
    (3, 1, 2) : 7,
    (2, 1, 3) : 8,
    (1, 1, 2) : 0,
    }

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())

    #중복체크
    dup_check = []
    #결과, 답
    result = 0

    #각 줄에 대해서 중복 처리를 위해 세트 사용
    arr = list(set([input()[:m] for _ in range(n)]))

    #각 줄에 대해서 코드 검사
    for i in range(len(arr)):
        #한 줄 가져오기
        row = arr[i]

        #16진수 문자열을 숫자로 바꾸고 이진수 문자열로 바꾸기
        bin_row = ""
        for c in row:
            # 한 글자씩 검사
            c_hex = int(c, 16)
            #16진수는 이진수*4의 길이
            for j in range(3, -1, -1):
                bin_row += "1" if c_hex & (1<<j) else "0"

        #이진수 문자열에 1이 없다면
        if "1" not in bin_row:
            continue
        #1이 있다면 암호 해독
        else:
            # 0 과 1의 비율
            ratio = [0] * 4
            # 0 1 0 1 순서대로
            # 모든 코드는 1로 끝나니 전체줄 오른쪽 0 모두 제거
            bin_row = bin_row.rstrip("0")
            new_code = []
            # 코드의 맨끝이 1이니 뒤부터 비율 세주기
            for j in range(len(bin_row) - 1, -1, -1):

                #마지막 1의 개수 세기
                if bin_row[j] == "1" and ratio[2] == 0:
                    ratio[3] += 1
                #세번째 0의 개수 세기
                elif bin_row[j] == "0" and ratio[1] == 0:
                    ratio[2] += 1
                #두번째 1의 개수 세기
                elif bin_row[j] == "1" and ratio[0] == 0:
                    ratio[1] += 1
                #첫번째 0과 왼쪽 코드 마지막 1이 만나는 지점에서
                elif bin_row[j] == "0" and bin_row[j-1] == "1":
                    # 최소 비율(최대 공약수) 계산
                    min_ratio = min(ratio[1:4])
                    number = decrypt[(ratio[1]//min_ratio, ratio[2]//min_ratio, ratio[3]//min_ratio)]
                    # 비율 계산 끝났으니 초기화
                    ratio = [0] * 4

                    new_code.append(number)
                    #현재 만든 코드의 길이가 8 이면
                    if len(new_code) == 8:
                        #검증 코드 계산
                        odd = new_code[1] + new_code[3] + new_code[5] + new_code[7]
                        even = new_code[0] + new_code[2] + new_code[4] + new_code[6]

                        # 계산 결과를 10으로 나눠어서 떨어지면 올바른 코드

                        if (odd*3 + even) % 10 == 0 and new_code not in dup_check:
                            # 각 자리수 더해서 저장
                            result += odd + even
                            # 중복처리
                            dup_check.append(new_code)
                        #만든 코드 초기화
                        new_code = []
    print(f"#{tc} {result}")

