from os import system
from random import choice

system("cls")

x = 20

while 1:
    try:
        y = int(input("Enter an integer: "))

        if x == y:
            print(choice([" x is equal y.", " y is equal x."]))
        elif x > y:
            print(choice([" x is greater than y.", " y is less than x."]))
        else:
            print(choice([" y is greater than x.", " x is less than y."]))
        break
    except ValueError:
        system("cls")
        continue