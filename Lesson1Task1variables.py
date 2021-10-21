# Поработайте с переменными, создайте несколько, выведите на экран, 
# запросите у пользователя несколько чисел и строк и 
# сохраните в переменные, выведите на экран.
from _typeshed import SupportsNoArgReadline


print("Эта программа задаст Вам несколько вопросов, а потом опишет, что произошло с Вашими ответами. Итак, начнём:")
someString = input("Введите, пожалуйста несколько букв Вашего алфавита в произвольном порядке ")
print("Проверьте, пожалуйста, точно ли ввели: ", someString)
anotherString = input("Введите, пожалуйста вторую строку ")
thirdString = input("И ещё одну введите, пожалуйста, чтобы действительно было несколько ")
print ("Итого получилось: " + someString + " " + anotherString + " " + thirdString)
someBool = False
someBool = bool(input("Если верно, введите что угодно и нажмите Enter, или просто нажмите Enter, если верно обратное "))
print("Что по-английски: ",someBool)
someInt = int(input("Теперь введите, пожалуйста, целое число, а другое не вводите, чтобы не проверять, поскольку, т.н. защиты от дурака не предусмотрено "))
print("Если в компе пока всё нормально с памятью, то Ваш ввод: ", someInt)
secondInt = int(input("And another one: "))
thirdInt = int(input('And one more to comply with the "several" criteria '))
print(F"Your sever integers are: {thirdInt} and {secondInt} and {someInt}")