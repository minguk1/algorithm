n = input()
def fn_d(n):
    number_sum = 0
    for i in list(n):
        number_sum = number_sum + int(i)



    generator = int(n) + number_sum

    return generator

print(fn_d(n))

t = input()
def is_selfnumber(t):
    generator_list = []
    for k in range(1, int(t)):
        generator_list.append(fn_d(str(k)))
    if int(t) not in generator_list:
        return "self_number"
    else:
        return "self_number 아님"

print(is_selfnumber(t))