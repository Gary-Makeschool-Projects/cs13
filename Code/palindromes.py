#!python

import string


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    clean = ''.join(e for e in text if text.isalnum()).lower()
    reverse = ''.join(reversed(clean))
    if (clean == reverse):
        return True
    return False


def is_palindrome_recursive(text, left=None, right=None):
    if len(text) < 1:
        return True
    else:
        # check if the left most and right most characters are the same
        if text[0] == text[-1]:
            # return the string but with those two characters removed
            return is_palindrome_recursive(text[1:-1])
        else:
            # return false
            return False


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
