#2. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.
# name, patr, birthyear, city, email, phone

def createUser(**kwargs):
    return kwargs

print (createUser(name=input("Name: "), patronymic=input("Patronymic: "), birthyear=input("Birthyear: "),
                     city=input("City: "), email=input("email: "), phone=input("Phone: ")))
