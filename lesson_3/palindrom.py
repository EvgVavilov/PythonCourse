word = input("Введите фразу: ")
rev_word = word.replace(" ","")
rev_word = rev_word[-1::-1]
if rev_word == word:
    print('Это палиндром')
else:
    print("Это не палиндом")
