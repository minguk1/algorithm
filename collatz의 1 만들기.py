# def collatz(num):
#     count = 0
#     while True:
#         if count == 500:
#             return -1
#             break
#         else:
#             if num%2 == 0:
#                 num = num / 2
#                 count += 1
#             else:
#                 num = num*3 + 1
#                 count += 1
#
#         if num == 1:
#             return count
#             break
#
# print(collatz(2**501))

class Collatz:
    def __init__(self,num):
        self.num = num

    def collatz(self):
        count = 0
        while True:
            if count == 500:
                return -1
                break
            else:
                if self.num%2 == 0:
                    self.num = self.num / 2
                    count += 1
                else:
                    self.num = self.num*3 + 1
                    count += 1

            if self.num == 1:
                return count
                break

    def __str__(self):
        return f"{self.collatz()}"


print(Collatz(16))
print(Collatz(27))

