right_number = 1234


i = 0
while i < 3:
    input_password = int(input())
    if right_number == input_password:
        print("pass")
        break
    else:
        i = i + 1