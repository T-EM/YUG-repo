# odd or even
from os import system
from random import choice
system("cls")

while 1:
    try:
        a: int = int(input("Enter an integer: "))
        even = "even"
        odd = "odd"
        print(f"{a} is {even if(a%2==0)else odd}")
        break
    except ValueError:
        system("cls")
        continue
