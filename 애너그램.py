# A.    입력 예시
# ['eat','tea','tan','ate','nat','bat']

# B.    출력 예시
# [ ['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat'] ]
b= input()
print(type(b))
print(b[1:-1])
a = list(b[1:-1].split(","))
print(a)
for word in a:
    word = word.replace("'", "")
print(a)
# for i in range(len(a)):
#     spelling = list(a[i])
#     print(spelling)

# def group_anagrams(a):
#     for i in a:
