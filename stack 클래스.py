class Stack:
    def __init__(self): #클래스 생성 시
        self.list = [] # 빈 리스트 생성

    def empty(self):
        if len(self.list) == 0: #비어 있을 때
            return True
        else:
            return False
        # return not bool(self.list) 한문장으로도 가능

    def top(self):
        if len(self.list) == 0:
            return None
        else:
            return self.list[-1] #인덱스를 이용해 리스트 마지막 원소 반환

    def pop(self):
        if len(self.list) == 0:
            return None
        else:
            return self.list.pop() #pop함수를 이용하여 마지막 원소 추출, 반환

    def push(self, x):
        self.list.append(x) #append로 마지막에 원소 추가

    def __repr__(self):
        return repr(self.list)

a = Stack()
print(a) #[]
a.push(5)  #리스트 마지막에 5 원소 추가
print(a.empty()) #False #5가 들어있으니 비어 있지 않음.
a.push(3) #3도 추가
print(a) #[5,3]
print(a.top()) #3 #가장 마지막 값 3 반환
print(a.pop()) #3 #가장 마지막 값인 3원소 추출하여 반환
print(a.pop()) #5 #남은 5도 추출하여 반환
print(a.empty()) #True #비어 있음.
print(a) #[]