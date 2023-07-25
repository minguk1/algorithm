class Calculator:

    def __init__(self, a, b):
        self._a = a
        self._b = b

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, new_b):
        if new_b == 0:
            print("0으로 바꿀 수 없습니다.")
            return

        self._b = new_b


    def divide(self):

        return self._a / self._b



c = Calculator(10, 5)
c.b = 10

print(c.divide())