a = "apple"
b = "banana"

def count_vowels(t):
    t_list = list(t)
    a_count = t_list.count("a")
    e_count = t_list.count("e")
    i_count = t_list.count("i")
    o_count = t_list.count("o")
    u_count = t_list.count("u")
    count_sum = a_count + e_count + i_count + o_count + u_count
    # vowel_count = t_list.count("a","e")
    return count_sum

print(count_vowels("aekmfaioiaf"))