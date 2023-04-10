# to check if the number is divisible by 5 and 6

x = int(input("Enter the number: "))

# for i in range (1,n+1):

if x % 5 == 0:
    print(f" {x} is divisible by 5" )

elif x % 6 == 0:
    print(f" {x} is divisible by 6")

else :
    print(f" {x} is not divisible by 5 and 6")