# electricity usage bill generator
# units 0 to 50, Rate=2.60, SC=25
# units 51 to 100, Rate=3.25, SC=35
# units 101 to 200, Rate=5.26, SC=45
# units 200+, Rate=8.45, SC=75

# units = 150

x = float(input("Enter the number of units: ")) #number of Units
sum: float = 0.0

if x >= 50: # units 0 to 50, Rate=2.60, SC=25
    print("Pass 1")
    if x > 50:
        sum += 50 * 2.60
    else:
        sum += x * 2.60 + 25
if x >= 51: # units 51 to 100, Rate=3.25, SC=35
    print("Pass 2")
    if x > 100:
        sum += 100 * 3.25
    else:
        sum += (x-50) * 3.25 + 35
if x >= 101: # units 101 to 200, Rate=5.26, SC=45
    print("Pass 3")
    if x > 200:
        sum += 200 * 5.26
    else:
        sum += (x-100) * 5.26 + 45
if x > 200: # units 200+, Rate=8.45, SC=75
    print("Pass 4")
    sum += (x-200) * 8.45 + 75

print(f"Your bill amount is {sum}")