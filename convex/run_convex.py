#!/usr/bin/env -S python3 -B
from r2point import R2Point
from convex import Void
from modification import Circle_perimeter

f = Void()
d = Circle_perimeter()
try:
    X = float(input("Введите x координату центра круга -> "))
    Y = float(input("Введите x координату центра круга -> "))
    R = float(input("Введите значение радиуса -> "))
    while True:
        f = f.add(R2Point())
        print(f"S = {f.area()}, P = {f.perimeter()}")
        ans = d.Perimeter_recount(f, X, Y, R)
        print(f"P части выпуклой оболочки внутри замкнутого круга = {ans}")
        print()
except (EOFError, KeyboardInterrupt):
    print("\nStop")
