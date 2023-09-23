T = int(input())
word_set = set()
for i in range(T):
    word = input()
    word_set.add(word)


word_list = list(word_set)
result_list = sorted(word_list)


len_list = []
for a in result_list:
    len_list.append(len(a))


for i in range(1, max(len_list)+1):
    for b in result_list:
        if len(b) == i:
            print(b)


