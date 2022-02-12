# импорт модулей проекта
from colorama import Fore, Back 
from colorama import init
init()
# сам код программы 
print(Fore.MAGENTA)
EMail = input("Введите логин или адрес электорнной почты: ")
password = input("Введите пароль здесь: ")
password_1 = list(password)
while len(password_1) < 8:
    print(Fore.RED)
    print("Пароль должен содержать не менее 8 символов!")
    print(Fore.MAGENTA)
    password = input("Введите пароль здесь: ")
    password_1 = list(password)
else:
    users = []
    users.append([password, EMail])
    print(Fore.GREEN)
    print(users)
    print("Успешно!")
input()