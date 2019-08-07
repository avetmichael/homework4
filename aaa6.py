import math

z = float(input("mutqagreq z: "))
x = float(input("mutqagreq x: "))

if 1 <= x <= 7:
    print("f(x) =", math.pow(math.fabs(x) + 2*math.fabs(z), 1/4) + math.pow(math.e, math.fabs(x + 1)))

else:
    print("f(x) =", math.tan((pow(x + z, 7))**2))

#18

