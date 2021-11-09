#5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
#initial:
totalSum = 0

while True:
    #vvod
    userString = input("Please input some integers separated by blank space to calculate sum or 'z' to exit: ")
    #razbivka
    conList = userString.split()
    listLen = len(conList)
    #summ_if
    el = 'z'
    for any in conList:
        #sum the list elements until el is met
        if any == 'z':
            print(f"'z' is found Final sum is {totalSum}")
            quit()
        else:
            try:
                totalSum += int(any)
            except ValueError:
                print(f"Some fuzzy input, but the sum so far is {totalSum}")
                quit()
                break
        print(f"Interim sum is {totalSum}") #added for debugging purposes you can delete or comment out this line afterwards

print(f'The total sum is {totalSum}')
