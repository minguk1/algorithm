# def f1(x):
#     a = 3
#     b = 5
#     y = a*x + b
#     print(y)
#
# d = f1(10)
#
# print(d)

# 1번
# a = int(input())
# def number(b):
#     if b == 1:
#         return "일"
#     elif b == 2:
#         return "이"
#     elif b == 3 :
#         return "삼"
#
# print(number(a))
#
# def quiz():
#     ans = input("1+2 = ")
#     print (1 + 2 == int(ans))
#
# quiz()

#연습 2번
# score = [ 0, 0, 2, 4, 7, 7, 9, 11, 11, 13, 18, 20]

# stem_leaf = [[], [], []]
#
# for s in score:
#     d, m = divmod(s, 10)
#     print(d, m)
#     stem_leaf[d].append(m)
# print(stem_leaf)

# dict = { "학용품" : "연필", }
# # result[a] = result.get(a,[])+[i]
# dict["학용품"] += dict.get("학용품","지우개")
# # dict.get("c", "a")
#
# print(dict)

# a = [1, 2, 3, 4, 1, 2]
# b= set(a)
# print(b)
lst=['eat','ate','tea','nat','tan','bat']
result= {}
for i in lst:
    a=''.join(sorted(i))
    print(a)
    result[a] = result.get(a,[])+[i]
print(result.values())