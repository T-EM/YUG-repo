# finding the largest among 3 numbers
from os import system
from random import choice
system("cls")

while 1:
    try:
        a:int = int(input("Enter an integer: "))
        b:int = int(input("Enter an integer: "))
        c:int = int(input("Enter an integer: "))

        print(f"Greatest integer is {(c if(c > a) else a)if(a > b)else(c if(c > b) else b)}")
        break
    except ValueError:
        system("cls")
        continue