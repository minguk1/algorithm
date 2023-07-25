# 1 + 2 1, "+", 2
# 2 – 1
# 3 * 4
# 4 / 0

a = list(input().split())


class Calculator:
    def __init__(self, input_list):
        self.num1 = int(input_list[0])
        self.num2 = int(input_list[2])
        self.symbol = input_list[1]



    def add(self):
        return f"{self.num1+self.num2}"

    def substract(self):
        return f"{self.num1-self.num2}"

    def multiply(self):
        return f"{self.num1*self.num2}"

    def divide(self):
        if self.num2 == 0:
            return "0으로 나눌 수 없습니다."
        else:
            return f"{self.num1 / self.num2}"


    def __str__(self):
        if self.symbol == "+":
            return f"{self.add()}"
        elif self.symbol == "-":
            return f"{self.substract()}"
        elif self.symbol == "*":
            return f"{self.multiply()}"
        elif self.symbol == "/":
            return f"{self.divide()}"


print(Calculator(a))




