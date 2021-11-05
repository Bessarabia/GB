#6. Реализовать функцию int_func(), принимающую слово
# из маленьких латинских букв
# и возвращающую его же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.
#Продолжить работу над заданием. В программу должна попадать строка из слов,
# разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().

def int_func(text):
    text = text.capitalize()
    return text

someText = input("Input a word: ")
print(someText)
print(int_func(someText))

someString = input("Ok? Then input some phrase: ")
splitString = someString.split()

counter = 0
while counter < len(splitString):
    try:
        capWord = int_func(splitString[counter])
        splitString[counter] = capWord
        #print(splitString)
        counter += 1
    except ValueError:
        break

print(*splitString)
