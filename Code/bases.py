#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)
    >>> decode(-13, 4)
    '-31'
    >>> decode(91321, 2)
    '10110010010111001'
    >>> decode(791321, 36)
    'gyl5'
    >>> decode(91321, 2, 'ab')
    'babbaabaababbbaab'
    """
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    #############  edited version of kevins god tier code (removed pow) ##########
    CONVERT_STRING = string.digits + string.ascii_lowercase
    BASE_DECODE = {digit: val for val, digit in enumerate(CONVERT_STRING)}
    decoded = 0
    for i, digit in enumerate(reversed(digits)):
        decoded += ((base**i) * BASE_DECODE[digit])
    return decoded
    #############  edited version of kevins god tier code (removed pow) ##########

    # my pretty lame code
    # decoded = 0  # product
    # # base ^ n
    # n = len(digits) - 1
    # # check each number in digit and raise it to ^n
    # for num in digits:
    #     # digit (base 10)
    #     digit = (CONVERT_STRING.index(num) * (base ** n))
    #     # add that value to our total
    #     decoded += digit

    #     n -= 1  # inverse of encode where encode is log base n decode is base raised to the n

    # return decoded  # product


def encode(number, base, numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
    """Encode given number in base 10 to digits in given base.
    number: int - - integer representation of number(in base 10)
    base: int - - base to convert to
    return: str - - string representation of number(in given base)
    Change a  to a base-n number.
    Up to base-36 is supported without special notation.
    convert positive decimal integer n to equivalent in another base(2-36)
    >> > encode(-13, 4)
    '-31'
    >> > encode(91321, 2)
    '10110010010111001'
    >> > encode(791321, 36)
    'gyl5'
    >> > encode(91321, 2, 'ab')
    'babbaabaababbbaab'
    """
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    if number == 0:
        return "0"

    if number < 0:
        return '-' + encode((-1) * number, base, numerals)

    if not 2 <= base <= len(numerals):
        raise ValueError('Base must be between 2-%d' % len(numerals))

    left_digits = number // base
    if left_digits == 0:
        return numerals[number % base]
    else:
        return encode(left_digits, base, numerals) + numerals[number % base]


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str - - string representation of number(in base1)
    base1: int - - base of given number
    base2: int - - base to convert to
    return: str - - string representation of number(in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    if base1 == 10:
        return encode(int(digits), base2)
    return encode(decode(digits, base1), base2)


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(
            digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()
