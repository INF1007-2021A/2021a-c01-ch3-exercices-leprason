#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math


def square_root(a: float) -> float:
    a = math.sqrt(a)
    return a


def square(a: float) -> float:
    a *= a
    return a


def average(a: float, b: float, c: float) -> float:
    x = a + b + c
    x /= 3
    return x


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    x = angle_degs + (angle_mins + angle_secs / 60) / 60
    x = math.radians(x)
    return x


def to_degrees(angle_rads: float) -> tuple:
    r = angle_rads*180/math.pi
    m = (r - int(r))*60
    s = (m - int(m))*60
    return int(r), int(m), int(s)


def to_celsius(temperature: float) -> float:
    x = (temperature - 32) * 5 / 9
    return x


def to_farenheit(temperature: float) -> float:
    x = (temperature * 9 / 5) +32
    return x


def main() -> None:
    print(f"La racine carré de 144 est : {square_root(144)}")

    print(f"Le carré de 12 est : {square(12)}")

    print(f"Moyenne des nombres 2, 4, 6: {average(2, 4, 6)}")

    print(f"Conversion de 100 degres, 2 minutes et 45 secondes en radians: {to_radians(100, 2, 45)}")

    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()
