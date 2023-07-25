# words = ["round" , "dream", "magnet" , "tweet" , "tweet", "trick", "kiwi"]
#
# repeat = []
#
# for i in range(1, len(words)):
#     # print(words[i])
#     # print(words[i] in repeat)
#     # repeat.append(words[i])
#     if (words[i] in repeat) or (words[i][0] != words[i-1][len(words[i-1])-1]):
#
#         print(i+1)
#         break
#     else :
#         repeat.append(words[i])

#교수님 코드
words = ["round" , "dream", "magnet" , "tweet" , "tweet", "trick", "kiwi"]

for idx in range(len(words)):
    if (words[idx][-1] != words[idx + 1][0]) or (words[idx] in words[:idx]):
        print(idx+1)
        break