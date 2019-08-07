import math

a = float(input("mutqagreq a: "))
x = float(input("mutqagreq x: "))

if math.fabs(a) < 3:
    print("f(x) =", math.sin(math.fabs(x + a)**2) + math.cos(x**2)**2)

else:
    print("f(x) =", (a**2 + x**2)**1/4 * math.log(a**2 + x**4, 2))

#16

