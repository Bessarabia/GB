# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

totalSum = 0
userString = input("Please input some integers separated by blank space to calculate  sum or 'z' to exit: ")
conList = userString.split()

lenList = len(conList)
counter1 = 0

while True:
    try:
        s = int(conList[counter1])
        totalSum += s
        counter1 += 1
        print(totalSum)
    except ValueError:
        print("incorrect input")
    break
    finally:
        userString = input("Please input some integers separated by blank space to calculate  sum or 'z' to exit: ")
        conList = userString.split()
        lenList = len(conList)
        counter1 = 0

print(totalSum)
