# find all the divisors of an integer

x = int(input("Enter the number: "))
for i in range(1,x+1):
    if x % i == 0:
        print(f"{i} is divisor of {x}" )
