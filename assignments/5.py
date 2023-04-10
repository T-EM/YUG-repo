# Sum of Digit of Numbers

x = 9834059799
sum = 0

while x != 0 :
    rem = x % 10
    sum = sum + rem
    x //= 10
print("Sum of Digit of Numbers is: " + str(sum))