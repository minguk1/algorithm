def simple_strcmp(s1, s2):
    a = ord(s1)
    b = ord(s2)

    return a-b


print(simple_strcmp("G", "A"))

def itoa(n):
    k = ""
    t = len(str(n))
    for i in range(t):
        a = n%10
        b = chr(a+48)
        k = k + b
        n = n // 10
    return k[::-1]


print(itoa(168))
print(type(itoa(168)))