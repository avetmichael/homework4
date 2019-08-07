import math


a = float(input("mutqagreq a: "))
b = float(input("mutqagreq b: "))
x = float(input("mutqagreq x: "))

if a < 3:
    print("f(x) =", math.pow(math.e, math.cos(x + a + b)) * math.tan(a + b**2))

else:
    print(math.log(4 + a**2 + b**2, 3))


#20