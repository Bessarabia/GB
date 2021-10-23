# Пользователь вводит целое положительное число. 
# Найдите самую большую цифру в числе. 
# Для решения используйте цикл while и арифметические операции.
# get the string, get the length of the string, cycle through the length comparing digit by digit, print the maxDigit

userInput = input("Provide the number: ")
loopCounter = len(userInput) - 1
userInt = int(userInput)
maxDigit = userInt % 10

while loopCounter > 0:
  digit = userInt % 10
  userInt = (userInt - digit)/10
  maxDigit = max(digit, maxDigit)
  loopCounter = loopCounter - 1
  continue

print ("Maximal digit is %d" % maxDigit)
