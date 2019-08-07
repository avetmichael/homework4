import math


a = float(input("mutqagreq a: "))
b = float(input("mutqagreq b: "))
x = float(input("mutqagreq x: "))

if a + math.fabs(b) < -5:
    print("f(x) =", math.pow(math.e, math.fabs(a + x)) * math.pow(math.cos(a + x + b), 2))

elif a + math.fabs(b) > 2:
    print("f(x) =", math.pow(math.atan(a + x), 1/3))

else:
    print("f(x) =", a + math.fabs(b))

#13
