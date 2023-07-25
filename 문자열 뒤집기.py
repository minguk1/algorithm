def my_reverse(string):
    n = len(string)
    if n%2 == 1:
        k = int(n/2)
        string_list = list(string)
        for i in range(1, k+1):
            string_list[k-i], string_list[k+i] = string_list[k+i], string_list[k-i]
        result = ''.join(string_list)
        return result
    else:
        k = int(n/2)
        string_list = list(string)
        for i in range(1, k+1):
            string_list[k-i], string_list[k+i-1] = string_list[k+i-1], string_list[k-i]
        result = ''.join(string_list)
        return result
print(my_reverse("abcd"))