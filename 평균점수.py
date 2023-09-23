s = input('숫자를 입력해주세요 : ')
s_list = list(s)

sum = 0
for i in s_list:
    sum = sum + int(i)
print(sum)