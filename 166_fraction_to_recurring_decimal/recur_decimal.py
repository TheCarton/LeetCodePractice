class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        sign = "-" if numerator / denominator < 0 else ""
        numerator = abs(numerator)
        denominator = abs(denominator)
        decimal_string = "{}{}".format(sign, numerator // denominator)
        remainder = numerator % denominator
        if remainder == 0:
            return decimal_string
        decimal_string += "."
        remainders = dict()
        while remainder not in remainders:
            remainders[remainder] = len(decimal_string)

            dividend = remainder * 10 // denominator
            remainder = remainder * 10 % denominator
            decimal_string += "{}".format(dividend)
            if remainder == 0:
                return decimal_string

        left_paren_index = remainders[remainder]
        decimal_string = decimal_string[:left_paren_index] + "(" + decimal_string[left_paren_index:] + ")"
        return decimal_string


s = Solution()


def whole_number():
    r = s.fractionToDecimal(2, 2)
    c = "1"
    print(f"got: {r}\ncor: {c}")


def half():
    r = s.fractionToDecimal(1, 2)
    c = "0.5"
    print(f"got: {r}\ncor: {c}")


def my_example():
    r = s.fractionToDecimal(5, 74)
    c = "0.0(675)"
    print(f"got: {r}\ncor: {c}")


def case_3():
    r = s.fractionToDecimal(4, 333)
    c = "0.(012)"
    print(f"got: {r}\ncor: {c}")


def main():
    whole_number()
    half()
    my_example()
    case_3()


main()
