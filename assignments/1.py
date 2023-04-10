# find the largest of two numbers 
from os import system
from random import choice


while 1:
    try:
        a:int = int(input("Enter an integer: "))
        b:int = int(input("Enter an integer: "))

        if a == b:
            print(choice([" a is equal b.", " b is equal a."]))
        elif a > b:
            print(choice([" a is greater than b.", " b is less than a."]))
        else:
            print(choice([" b is greater than a.", " a is less than b."]))
        break
    except ValueError:
        system("cls")
        continue