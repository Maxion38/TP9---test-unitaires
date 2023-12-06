from tp7 import Fraction

if __name__ == '__main__':

    f3 = Fraction(8, 3)

    print("str f3")
    print(f3)
    print("")

    print("mixed number f3")
    print(f3.as_mixed_number())
    print("")


    f1 = Fraction(2, 8)
    f2 = Fraction(5, 8)

    print("Reduced f1   Reduced f2")
    print(str(f1) + "          " + str(f2))
    print("")

    print("Operations")
    print("__________")
    print("add")
    print(f1 + f2)
    print("")

    print("sub")
    print(f1 - f2)
    print("")

    print("mul")
    print(f1 * f2)
    print("")

    print("truediv")
    print(f1 / f2)
    print("")

    print("pow")
    print(Fraction(2, 1) ** Fraction(3,1))
    print("")


    print("Boolean")
    print("_______")

    print("eq")
    print(Fraction(1, 4) == (Fraction(2, 8)))
    print("")

    print("isZero")
    print(Fraction(0, 4).is_zero())
    print("")

    print("isInt")
    print(Fraction(4, 2).is_integer())
    print("")

    print("isProper")
    print(Fraction(2, -4).is_proper())
    print("")

    print("isUnit")
    print(Fraction(4, 4).is_unit())
    print("")

    print("isAdjacent")
    print(Fraction(-6, 4).is_adjacent_to(Fraction(2, 4)))
    print("")
