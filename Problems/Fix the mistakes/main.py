text = input()

words_list = text.split()
for i in range(len(words_list)):
    if 'www.' in words_list[i].casefold() or 'https://' in words_list[i].casefold() \
        or 'http://' in words_list[i].casefold():
        print(words_list[i])
