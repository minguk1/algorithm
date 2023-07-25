n = int(input())
n_list = [i for i in range(n, 0, -1)]
input_list = []
for i in range(n):
    input_list.append(int(input()))
# print(n_list)
stack = [] #스택 생성
result ="" # +와 - 를 모아주기 위한 문자열 생성
i = 0
while True:

    if stack: #스택이 있을 때
        if stack[-1] == input_list[i]: #그 스택 마지막 원소가 원하는 값일 때
            trash = stack.pop() # 스택에서 그 원소를 빼줍니다.
            i += 1
            result += "-"

        elif n_list: #스택이 있지만 마지막 원소가 원하는 값이 아닐 때, 계속 정수 리스트에서 추출
            b = n_list.pop()
            stack.append(b)
            result += "+"
        elif len(n_list) == 0: #스택이 있지만 마지막 원소가 원하는 값이 아니고 정수 리스트도 비었을 때
            # 더 이상 스택 진행 불가능 NO 출력
            result = "NO"
            break

    else: #스택이 없을 때 정수 리스트에서 스택으로 빼오기
        a = n_list.pop()
        stack.append(a)
        result += "+"
    if len(n_list) == 0 and len(stack) == 0: # 두 리스트 다 비웠을 때 끝내기
        break
if result == "NO": #실행이 불가능 할 때 NO 출력
    print(result)
else: #지금까지 모은 + - 순서대로 출력
    for i in range(len(result)):
        print(result[i])



