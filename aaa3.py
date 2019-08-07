import math


a = float(input("mutqagreq a: "))
b = float(input("mutqagreq b: "))
x = float(input("mutqagreq x: "))


if a**2 + b**2 > 5:
    print("f(x) =", 3*math.pow(math.e, a - x) + math.log(a**2 + b**2 + 5, 3))

elif a**2 + b**2 < 1:
    print("f(x) =", math.pow(math.tan(a + b), 4))

else:
    print("f(x) =", -3)

#11