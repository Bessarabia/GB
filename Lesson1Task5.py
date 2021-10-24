#5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

earnings = int(input("Please input earnings: "))
totalCost = int(input("Please input total costs: "))
finResult = earnings - totalCost

if finResult > 0:
    print ("Reported profit of %d" % finResult)
    grossMargin = finResult / earnings
    numEmployees = int(input("Please input headcount: "))
    profPE = finResult / numEmployees
    print("Your profit per employee is %d" % profPE)
elif finResult == 0:
    print("Break-even observed, watch out")
else:
    print("Reported loss of %d" % finResult)
