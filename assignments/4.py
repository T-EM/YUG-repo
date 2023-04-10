# Reverse the number

x = 9834059799
rev = 0

while x != 0 :
    rem = x % 10
    rev = rev * 10 + rem
    x //= 10
print("the reversed number is: " + str(rev))
