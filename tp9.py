import unittest
from tp7 import *


class FractionTestCase(unittest.TestCase):
    # Init test
    def test_init(self):
        frac1 = Fraction(2, 4)
        self.assertEqual(frac1.get_num, 1)
        self.assertEqual(frac1.get_den, 2)

        # zeros
        self.assertEqual(Fraction(0, 4), Fraction(0, 1))
        self.assertRaises(ZeroDivisionError, Fraction, 4, 0)

        # fractions négatives
        self.assertEqual(Fraction(-2, 4), Fraction(-1, 2))
        self.assertEqual(Fraction(2, -4), Fraction(-1, 2))

        # not a number
        self.assertRaises(NotANumberException, Fraction, "a", 2)
        self.assertRaises(NotANumberException, Fraction, 2, "a")

# Methods test
    def test_str_method(self):
        self.assertEqual(Fraction(1, 2).__str__(), "1/2")
        self.assertEqual(Fraction(4, -2).__str__(), "-2/1")

    def test_mixed_number_method(self):
        self.assertEqual(Fraction(3/2).as_mixed_number(), "1 1/2")
        self.assertEqual(Fraction(4, 2).as_mixed_number(), "2")
        self.assertEqual(Fraction(2, 4).as_mixed_number(), "1/2")

# Operators test
    def test_add_operator(self):
        self.assertEqual(Fraction(1, 2).__add__(Fraction(1, 2)), Fraction(2, 2))
        self.assertEqual(Fraction(1, 4) + Fraction(2, 4), Fraction(3, 4))
        self.assertRaises(NotFractionInstanceException, Fraction(1, 2).__add__, 2)

    def test_sub_operator(self):
        self.assertEqual(Fraction(3, 4).__sub__(Fraction(1, 8)), Fraction(5, 8))
        self.assertEqual(Fraction(2, 4) - Fraction(1, 4), Fraction(1, 4))
        self.assertRaises(NotFractionInstanceException, Fraction(1, 2).__sub__, 2)

    def test_mul_operator(self):
        self.assertEqual(Fraction(3, 4).__mul__(Fraction(1, 8)), Fraction(3, 32))
        self.assertEqual(Fraction(2, 4) * Fraction(1, 4), Fraction(1, 8))
        self.assertRaises(NotFractionInstanceException, Fraction(1, 2).__mul__, 2)

    def test_truediv_operator(self):
        self.assertEqual(Fraction(1, 4).__truediv__(Fraction(5, 8)), Fraction(2, 5))
        self.assertEqual(Fraction(1, 4) / Fraction(2, 4), Fraction(1, 2))
        self.assertRaises(NotFractionInstanceException, Fraction(1, 2).__truediv__, 2)
        self.assertRaises(ZeroDivisionError, Fraction(1, 2).__truediv__, Fraction(0, 4))

    def test_pow_operator(self):
        self.assertEqual(Fraction(2, 1).__pow__(Fraction(3, 1)), Fraction(8, 1))
        self.assertEqual(Fraction(2, 1) ** Fraction(3, 1), Fraction(8, 1))
        self.assertRaises(NotFractionInstanceException, Fraction(1, 2).__pow__, 2)

    def test_decimal_value(self):
        self.assertEqual(Fraction(1, 2).__float__(), 0.5)

# Booleen test
    def test_eq_operator(self):
        self.assertEqual(Fraction(2, 8).__eq__(Fraction(1, 4)), True)
        self.assertEqual(Fraction(2, 8) == Fraction(1, 2), False)
        self.assertRaises(NotFractionInstanceException, Fraction(1, 2).__eq__, 2)

    def test_is_zero(self):
        self.assertEqual(Fraction(0, 8).is_zero(), True)
        self.assertEqual(Fraction(1, 8).is_zero(), False)

    def test_is_integer(self):
        self.assertEqual(Fraction(4, 8).is_integer(), False)
        self.assertEqual(Fraction(8, 8).is_integer(), True)
        self.assertEqual(Fraction(8, 4).is_integer(), True)

    def test_is_proper(self):
        self.assertEqual(Fraction(1, 4).is_proper(), True)
        self.assertEqual(Fraction(8, 4).is_proper(), False)

    def test_is_unit(self):
        self.assertEqual(Fraction(1, 8).is_unit(), True)
        self.assertEqual(Fraction(3, 8).is_unit(), False)

    def test_is_adjacent(self):
        self.assertEqual(Fraction(-6, 4).is_adjacent_to(Fraction(2, 4)), True)
        self.assertEqual(Fraction(4, 4).is_adjacent_to(Fraction(1, 4)), False)
        self.assertRaises(NotFractionInstanceException, Fraction(1, 2).is_adjacent_to, 2)
        