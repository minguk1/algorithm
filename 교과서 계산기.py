

icp = {"+":1, "-":1, "/":2,"*":2,"(":3}
isp = {"+":1, "-":1, "/":2,"*":2,"(":0}






def get_postfix(infix, n):
    #infix : 중위 표기식
    #n : 식의 길이
    stack = []
    postfix = "" #결과로 출력할 후위 표기식
    for i in range(n):
        if "0" <= infix[i] <= "9": # 숫자인 것 구분 피연산자
            postfix += infix[i]
        else:
            #닫는 괄호가 나오는 경우
            if infix[i] == ")":
                # 여는 괄호가 나올 때까지 pop하여 결과 출력
                while stack:
                    char = stack.pop()
                    if char == "(":
                        break
                    postfix += char

            #다른 연산자가 나오는 경우
            else:
                # 현재 토큰의 우선순위보다 stack top의 우선순위가 높거나 같으면 계속 pop
                while stack and isp[stack[-1]] >= icp[infix[i]]:
                    postfix += stack.pop()


                #그게 아니면 push
                stack.append(infix[i])

    while stack:
        postfix += stack.pop()

    return postfix

infix = "2+3*4/5"
n = len(infix)
print(get_postfix(infix,n))

def get_result(postfix):
    stack = []
    for c in postfix:

    #피연산자 만나면 스택에 넣기
        if "0" <= c <= "9":
            stack.append(int(c))
    #연산자 만나면 피연산자 두 개 꺼내서 계산
        else:
            right = stack.pop()
            left = stack.pop()

            if c == "+":
                result = left + right

            elif c == "-":
                result = left - right

            elif c == "*":
                result = left * right
            else:
                result = left / right

            stack.append(result)
    #마지막에 남은 결과 하나 꺼내서 리턴
    return stack.pop()

postfix = "234*5/+"
print(get_result(postfix))