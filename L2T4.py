# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

txt = input("Please input words separated by spaces and hit Enter: ")

spisokSlov = []
spisokSlov = txt.split(" ")
# print(spisokSlov)

listLen = len(spisokSlov)
iterator = 1

while iterator < listLen+1:
    numstr = str(iterator)  # type: str
    chunk = str(spisokSlov[iterator-1])
    if len(chunk) > 10: chunk = chunk[:10]
    print(f'{numstr}{" "}{chunk}')
    iterator += 1
