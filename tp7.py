# Exceptions
class NotANumberException(Exception):
    pass
class NotFractionInstanceException(Exception):
    pass


class Fraction:
    """Class representing a fraction and operations on it

    Author : Bongartz Maxime
    Date : November 2023
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num=0, den=1):
        """This builds a fraction based on some numerator and denominator.

        PRE : No specific preconditions
        POST : Simplified num and simplified den represent the reduced fraction form
        RAISES : NotANumberException if num or den are not numbers (float or int)
                 ZeroDivisionError if den == 0
        """

        if not(isinstance(num, (float, int))) or not(isinstance(den, (float, int))):
            raise NotANumberException("Fraction must be composed of numbers")

        if den == 0:
            raise ZeroDivisionError

        self.__num = num
        self.__den = den

        pgcd = self.__calc_pgcd()
        if pgcd == "numZero":
            self.__simplified_num = 0
            self.__simplified_den = 1
        else:
            sim_num = int(num / pgcd)
            sim_den = int(den / pgcd)
            if sim_den < 0:
                sim_num = 0 - sim_num
                sim_den = abs(sim_den)

            self.__simplified_num = sim_num
            self.__simplified_den = sim_den

    @property
    def num(self):
        return self.__simplified_num

    @property
    def den(self):
        return self.__simplified_den

    def __calc_pgcd(self):
        if self.__num < self.__den:
            small_num = self.__num
            big_num = self.__den
        else:
            small_num = self.__den
            big_num = self.__num

        rest = -1
        if small_num == 0:
            return "numZero"
        while rest != 0:
            rest = big_num % small_num
            big_num = small_num
            small_num = rest
        return big_num


    # ------------------ Textual representations ------------------

    def __str__(self):
        """Return a textual representation of the reduced form of the fraction

        PRE : No specific preconditions
        POST : Returns a str of the simplified num and den
        """
        return str(self.__simplified_num) + "/" + str(self.__simplified_den)


    def as_mixed_number(self):
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        PRE : No specific preconditions
        POST : Returns a str of the mixed fraction
        """

        den = self.__simplified_den
        num = self.__simplified_num
        whole = num // den
        rest = num % den
        if whole == 0 :
            proper_fraction = str(num) + "/" +str(den)

        else:
            if rest > 0 :
                proper_fraction = str(whole) + " " + str(rest) + "/" + str(den)
            else:
                proper_fraction = str(whole)

        return proper_fraction

    # ------------------ Operators overloading ------------------


    def __add__(self, other):
        """Overloading of the + operator for fractions

        PRE : No specific preconditions
        POST : Returns a new Fraction class representing the result of the addition
        RAISE : NotFractionInstanceException if "other" argument is not a Fraction class instance
        """
        if not(isinstance(other, Fraction)):
            raise NotFractionInstanceException("The operation must be between two Fraction class instances")

        num = self.__simplified_num
        den = self.__simplified_den
        num2 = other.num
        den2 = other.den
        num_result = num * den2 + num2 * den
        den_result = den * den2
        return Fraction(num_result, den_result)

    def __sub__(self, other):
        """Overloading of the - operator for Fractions

        PRE : No specific preconditions
        POST : returns a new Fraction class instance representing the result of the subtraction
        RAISE : NotFractionInstanceException if "other" argument is not a Fraction class instance
        """
        if not(isinstance(other, Fraction)):
            raise NotFractionInstanceException("The operation must be between two Fraction class instances")

        num = self.__num
        den = self.__den
        num2 = other.num
        den2 = other.den
        num_result = num * den2 - num2 * den
        den_result = den * den2
        return Fraction(num_result, den_result)

    def __mul__(self, other):
        """Overloading of the * operator for fractions

        PRE : No specific preconditions
        POST : returns a new Fraction class instance representing the result of the multiplication
        RAISE : NotFractionInstanceException if "other" argument is not a Fraction class instance
        """
        if not(isinstance(other, Fraction)):
            raise NotFractionInstanceException("The operation must be between two Fraction class instances")

        num = self.__num
        den = self.__den
        num2 = other.num
        den2 = other.den
        num_result = num * num2
        den_result = den * den2

        return Fraction(num_result, den_result)

    def __truediv__(self, other):
        """Overloading of the / operator for fractions

        PRE : No specific preconditions
        POST : returns a Fraction class instance representing the result of the division
        RAISE : NotFractionInstanceException if "other" argument is not a Fraction class instance
        """
        if not(isinstance(other, Fraction)):
            raise NotFractionInstanceException("The operation must be between two Fraction class instances")

        num = self.__num
        den = self.__den
        num2 = other.num
        den2 = other.den

        num_result = num * den2
        den_result = den * num2

        return Fraction(num_result, den_result)

    def __pow__(self, other):
        """Overloading of the ** operator for fractions

        PRE : No specific preconditions
        POST : Returns a float representing the result of the exponent
        RAISE : NotFractionInstanceException if "other" argument is not a Fraction class instance
        """

        if not(isinstance(other, Fraction)):
            raise NotFractionInstanceException("The operation must be between two Fraction class instances")

        num = self.__num
        den = self.__den
        num2 = other.num
        den2 = other.den

        num_result = num**(num2/den2)
        den_result = den**(num2/den2)

        return Fraction(num_result, den_result)

    def __eq__(self, other):
        """Overloading of the == operator for fractions

        PRE : No specific preconditions
        POST : Returns True if the fractions are equals else, return False
        RAISE : NotFractionInstanceException if "other" argument is not a Fraction class instance
        """
        if not(isinstance(other, Fraction)):
            raise NotFractionInstanceException("The operation must be between two Fraction class instances")

        num = self.__num
        den = self.__den
        num2 = other.__num
        den2 = other.__den
        return num * den2 == num2 * den

    def __float__(self):
        """Returns the decimal value of the fraction

        PRE : No specific preconditions
        POST : Returns the decimal value of the fraction
        """

        return self.num / self.den

    # TODO : [BONUS] You can overload other operators if you wish (ex : <, >, ...)


    # ------------------ Properties checking  ------------------

    def is_zero(self):
        """Check if a fraction's value is 0

        PRE : No specific preconditions
        POST : Returns True if num / den == 0 else returns False
        """
        return self.num == 0

    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRE : No specific preconditions
        POST : return True if the fraction is a round number, return False if not
        """
        num = self.__simplified_num
        den = self.__simplified_den

        return num / den % 1 == 0

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        PRE : No specific preconditions
        POST : return True if the absolute value of the fraction is < 1 return False if not
        """
        num = abs(self.__simplified_num)
        den = abs(self.__simplified_den)

        return num < den

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        PRE : No specific preconditions
        POST : return True if the simplified numerator is == 1 if not return False
        """
        return self.__simplified_num == 1

    def is_adjacent_to(self, other):
        """Check if two fractions differ by a unit fraction

        Two fractions are adjacent if the absolute value of the difference them is a unit fraction

        PRE : one other fraction
        POST : returns True if the fraction minus the other fraction simplified numerator is == 1 return False if not
        RAISE : NotFractionInstanceException if "other" argument is not a Fraction class instance
        """
        if not(isinstance(other, Fraction)):
            raise NotFractionInstanceException("The operation must be between two Fraction class instances")

        result_frac = Fraction(abs(self.__simplified_num), abs(self.__simplified_den)) - Fraction(abs(other.__simplified_num), abs(other.__simplified_den))

        return result_frac.is_unit()