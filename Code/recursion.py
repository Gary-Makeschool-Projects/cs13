#!python


def factorial(n):
    """factorial(n) returns the product of the integers 1 through n for n >= 0,
    otherwise raises ValueError for n < 0 or non-integer n"""
    # check if n is negative or not an integer (invalid input)
    if not isinstance(n, int) or n < 0:
        raise ValueError('factorial is undefined for n = {}'.format(n))
    # implement factorial_iterative and factorial_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return factorial_iterative(n)
    # return factorial_recursive(n)


def factorial_iterative(n):
    """factorial_iterative(n) iterativley returns the product of the integers 1 through n for n >= 0,
    otherwise raises ValueError for n < 0 or non-integer n
    >>> factorial_iterative(15) 
    1307674368000
    >>> factorial_iterative(20) 
    2432902008176640000
    >>> factorial_iterative(25) 
    15511210043330985984000000
    >>> factorial_iterative(30) 
    265252859812191058636308480000000
    """
    product = 1
    for i in range(1, n + 1):
        product = product * i
    return product


def factorial_recursive(n):
    """factorial_recursive(n) recursivley returns the product of the integers 1 through n for n >= 0,
    otherwise raises ValueError for n < 0 or non-integer n
    >>> factorial_iterative(15) 
    1307674368000
    >>> factorial_iterative(20) 
    2432902008176640000
    >>> factorial_iterative(25) 
    15511210043330985984000000
    >>> factorial_iterative(30) 
    265252859812191058636308480000000
    """
    # check if n is one of the base cases
    if n == 0 or n == 1:
        return 1
    # check if n is an integer larger than the base cases
    elif n > 1:
        # call function recursively
        return n * factorial_recursive(n - 1)


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 1:
        num = int(args[0])
        result = factorial(num)
        print('factorial({}) => {}'.format(num, result))
    else:
        print('Usage: {} number'.format(sys.argv[0]))


if __name__ == '__main__':
    main()
