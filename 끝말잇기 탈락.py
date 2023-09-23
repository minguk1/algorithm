words = ["round" , "dream", "magnet" , "tweet" , "twet", "prick", "kiwi"]
repeat = []

for i in range(1, len(words)):

    if (words[i] in repeat) or (words[i][0] != words[i - 1][len(words[i - 1]) - 1]):

        print(i + 1)
        break
    else:
        repeat.append(words[i])