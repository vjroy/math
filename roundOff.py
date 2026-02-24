from decimal import Decimal
import math
print(0.1 + .2)
#Prints .3(lots of 0's)4 due to round off

x = 0.1
print(x) #Misleading
print(format(x, ".20f"))

print(0.1 + 0.2 == 0.3)

a, b = Decimal(".1"), Decimal(".2")

print(math.isclose(0.1 + 0.2, 0.3))

a = math.inf
b = math.inf
print(a - b)
print(a)

c = math.nan
print(c != c) #Prints True - Wow!
