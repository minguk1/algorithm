import math
a=float(input("n1: "))
while True:

    b=float(input("n2: "))
    op = str(input("연산자: "))

    if a == 0 and b == 0:
        break

    if op == "+":
        print(a+b)
        c = int(input("계속 하시겠습니까?: "))
        if c == 0:
            break
        elif c == 1:
            a = a+b
        elif c == 2:
            a = int(input("n1: "))
    elif op == "-":
        print(a-b)
        c = int(input("계속 하시겠습니까?: "))
        if c == 0:
            break
        elif c == 1:
            a = a-b
        elif c == 2:
            a = int(input("n1: "))
    elif op == "*":
        print(a*b)
        c = int(input("계속 하시겠습니까?: "))
        if c == 0:
            break
        elif c == 1:
            a = a*b
        elif c == 2:
            a = int(input("n1: "))
    elif op == "/":
        print(round(a/b,3))
        c = int(input("계속 하시겠습니까?: "))
        if c == 0:
            break
        elif c == 1:
            a = a/b
        elif c == 2:
            a = int(input("n1: "))
    elif op == "//":
        print(a//b, a%b)
        c = int(input("계속 하시겠습니까?: "))
        if c == 0:
            break
        elif c == 1:
            a = a//b
        elif c == 2:
            a = int(input("n1: "))
    elif op == "%":
        print(f"{a/b*100}%")
        c = int(input("계속 하시겠습니까?: "))
        if c == 0:
            break
        elif c == 1:
            a = a/b*100
        elif c == 2:
            a = int(input("n1: "))
    elif op == "^":
        print(a**b)
        c = int(input("계속 하시겠습니까?: "))
        if c == 0:
            break
        elif c == 1:
            a = a**b
        elif c == 2:
            a = int(input("n1: "))
    elif op == "log":
        print(math.log(a, b))
        c = int(input("계속 하시겠습니까?: "))
        if c == 0:
            break
        elif c == 1:
            a = math.log(a, b)
        elif c == 2:
            a = int(input("n1: "))
    elif op == "sin":
        print(math.sin(a/180*math.pi))
        c = int(input("계속 하시겠습니까?: "))
        if c == 0:
            break
        elif c == 1:
            a = math.sin(a/180*math.pi)
        elif c == 2:
            a = int(input("n1: "))
    elif op == "cos":
        print(math.cos(a/180*math.pi))
        c = int(input("계속 하시겠습니까?: "))
        if c == 0:
            break
        elif c == 1:
            a = math.cos(a/180*math.pi)
        elif c == 2:
            a = int(input("n1: "))
    elif op == "tan":
        print(math.tan(a/180*math.pi))
        c = int(input("계속 하시겠습니까?: "))
        if c == 0:
            break
        elif c == 1:
            a = math.tan(a/180*math.pi)
        elif c == 2:
            a = int(input("n1: "))
    elif op == "phaser":
        print((a**2+b**2)**0.5, math.atan(a/b)*180/math.pi)
        c = int(input("계속 하시겠습니까?: "))
        if c == 0:
            break
        elif c == 1:
            a = (a**2+b**2)**0.5
        elif c == 2:
            a = int(input("n1: "))

    elif op == "complex":
        print(a*math.cos(b/180*math.pi),a*math.sin(b/180*math.pi))
        c = int(input("계속 하시겠습니까?: "))
        if c == 0:
            break
        elif c == 1:
            a = a*math.cos(b/180*math.pi)
        elif c == 2:
            a = int(input("n1: "))