line_list = list(map(int, input("s_triangle : ").split()))


# print(line_list)
# print(sorted(line_list))

a = sorted(line_list)[0]
b = sorted(line_list)[1]
c = sorted(line_list)[2]

# print(a, b, c)

if a == b == c:
    print("정삼각형")

elif a == b or b == c:
    print("이등변삼각형")

elif a**2 + b**2 == c**2:
    print("직각삼각형")

elif a + b > c:
    print("삼각형")

else:
    print("삼각형 아님")