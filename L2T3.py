# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

#[12,1,2,] [3,4,5] [6,7,8] [9,10,11]

listZ = [12,1,2]
listW = [3,4,5]
listL = [6,7,8]
listO = [9,10,11]

zima = dict.fromkeys(['1', '2', '12'], "зима")
vesna = dict.fromkeys(['3', '4', '5'], "весна")
leto = dict.fromkeys(['6', '7', '8'], "лето")
osen = dict.fromkeys(['9', '10', '11'], "осень")

userInt = input("Please input integer month number: ")

if zima.get(userInt) is not None: print(zima.get(userInt))
if vesna.get(userInt) is not None: print(vesna.get(userInt))
if leto.get(userInt) is not None: print(leto.get(userInt))
if osen.get(userInt) is not None: print(osen.get(userInt))
