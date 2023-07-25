#자동차 클래스 만들기
#자동차 클래스의 속성으로 자동차 총 수, 차량번호, 이름, 속도가 있다.
#자동차 클래스의 기능으로 자동차의 속도를 파라미터만큼 증가시키는 메서드와 감소시키는 메서드가 있다.
#자동차 클래스를 print를 통해 출력할 때 "이름 : 자동차이름, 차량번호 : 차량번호, 속도 : 속도"

class Car:
    total_number = 0

    def __init__(self, name, number, velocity):
        self.name = name
        self.number = number
        self.velocity = velocity
        Car.total_number += 1

    def up(self, v):
        self.velocity += v

    def down(self, v):
        self.velocity -= v

    def __str__(self):
        return f"이름 : {self.name}, 차량번호 : {self.number}, 속도 : {self.velocity}, 총수: {Car.total_number}"

    def __eq__(self, other): #비교할 때 차량번호를 기준으로 설정
        return self.number == other.number

one = Car("sonata", 1063, 80)
one.up(50)
two = Car("avante", 1063, 100)
print(one, two)
print(one == two)