UserWords = input("Введите слова: ")
words = UserWords.split(" ")
leight = list(map(len, words))
MaxLeight = max(leight)
pos = leight.index(MaxLeight)
print("Самое длинное слово - {}".format(words[pos]))
