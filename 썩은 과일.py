# a = "apple,rottenBanana,apple,Rottenorange,bAnana"
# lower_a = a.lower()
#
# list_a = list(lower_a.split(","))
# list_b = []
#
#
# for i in list_a:
#     if i[0:6] == "rotten":
#         list_b.append(i[6:])
#     else:
#         list_b.append(i)
# print(list_b)

#교수님 코드
fruit_bag = input("과일 봉지를 입력 : ").split(",")
fresh_bag = []
for fruit in fruit_bag:
    fruit = fruit.lower()

    fruit = fruit.replace("rotten" , "")
    fresh_bag.append(fruit)
print(fresh_bag)