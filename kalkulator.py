import math
from colorama import init
init()
from colorama import Fore, Back, Style
# основная часть кода
# ввод примера для вычислительных действаий
print(Fore.CYAN)
example = input('Действие: ')
# определение действия для подщёта
if example == "pi":
    print(Fore.GREEN)
    print(math.pi)
elif example != "pi":
    print(Fore.GREEN)
    print(example + ' = ' + str(eval(example)))
# добавление примера в общий список истори
exas = []
exas.append(example + ' = ' + str(eval(example)))

input() 