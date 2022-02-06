import math
from colorama import init
init()
from colorama import Fore, Back, Style

print(Fore.RED)
do = input(" действие: ")
 
 # арифметические действия

def plus(a, b):
    c = a + b
    print(c)

def minus(a, b):
    c = a - b
    print(c)

def mult(a, b):
    c = a * b
    print(c)

def div(a, b):
    c = a / b 
    print(c)

def degree(a,b):
    c = a ** b
    print(c)

if do == "pi":
    print(Fore.YELLOW)
    print(math.pi)
elif do != "pi":
    print(Fore.CYAN)
    x = float(input(" первое число: "))
    y = float(input(" второе число: "))
    if do == "+":  # действие"+"
        print(Fore.YELLOW)
        plus(x, y)
    elif do == "-":  # действие"-"
        print(Fore.YELLOW)
        minus(x, y)
    elif do == "*":  # дейтвие"*"
        print(Fore.YELLOW)
        mult(x, y)
    elif do == "/":  # действие"/"
        print(Fore.YELLOW)
        div(x, y)
    elif do == "**":  # возведение числа в степень
        print(Fore.YELLOW)
        degree(x, y )
    else:
        print(Fore.BLACK)
        print(" неверное действие, повторите попытку!")

input() 