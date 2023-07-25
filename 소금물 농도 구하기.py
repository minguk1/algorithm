salt_list = []
i = 0
while i < 5:
    # a = list(map(str, input().split()))
    a = input()
    if a == "done":
        break
    else:
        b = list(map(int, a.split()))
        salt_list.append(b)
        i = i + 1

print(salt_list)

salt_percentage = 0
liquid = 0

for k in range(len(salt_list)):
    liquid = liquid + salt_list[k][1]

for k in range(len(salt_list)):
    salt_percentage = salt_percentage + salt_list[k][0] * salt_list[k][1]

last_salt_percentage = round(salt_percentage / liquid, 2)

print(f"{last_salt_percentage}%")
print(f"{liquid}g")
