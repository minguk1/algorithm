

T = int(input())
for i in range(T):
    a = input()


    b = '.#.'.join(a)

    first = "#"*len(a)
    second = "#"*len(a)*2
    deco1 = ".."+'...'.join(first)+".."
    deco2 = "." + '.'.join(second)+"."
    print(deco1)
    print(deco2)

    print(f"#.{b}.#")
    print(deco2)
    print(deco1)
