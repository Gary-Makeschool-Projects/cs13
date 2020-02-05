#!python


def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    """
    Time Complexity
    ---------------
    Best Case: Ω(1) 
    Average Case: O(n)
    Worst Case: Θ(n) 

    If it is known that the target occurs once in the array, the best case of the
    iterative function will be at the initial index, this means at most n - 1 
    comparisons are needed and the expected number of comparisons is:
    (n+2)(n-1) / 2(n)
    ------------------------------------------------------

    names = ['Alex', 'Brian', 'Julia', 'Kojin', 'Nabil', 'Nick', 'Winnie']
    >>> linear_search_recursive('Alex')
    '0'
    >>> linear_search_recursive('Winnie')
    '6'
    >>> linear_search_recursive('Nick')
    '5'
    >>> linear_search_recursive('Brian')
    '1'
    """
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    """
    Time Complexity
    ---------------
    Best Case: Ω(1) 
    Average Case: O(n)
    Worst Case: Θ(n) 

    If it is known that the target occurs once in the array, the best case of the
    iterative function will be at the initial index, this means at most n - 1 
    comparisons are needed and the expected number of comparisons is:
    (n+2)(n-1) / 2(n)
    ------------------------------------------------------
    names = ['Alex', 'Brian', 'Julia', 'Kojin', 'Nabil', 'Nick', 'Winnie']
    >>> linear_search_recursive('Alex')
    '0'
    >>> linear_search_recursive('Winnie')
    '6'
    >>> linear_search_recursive('Nick')
    '5'
    >>> linear_search_recursive('Brian')
    '1'
    """
    # base case
    if index > len(array) - 1:
        return None
    else:
        # if array index holds target return index
        if item == array[index]:
            return index
    # otherwise increment index
    return linear_search_recursive(array, item, index + 1)


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    """
    names = ['Alex', 'Brian', 'Julia', 'Kojin', 'Nabil', 'Nick', 'Winnie']
    >>> binary_search_iterative(names, 'Alex')
    '0'
    >>> binary_search_iterative(names, 'Winnie')
    '6'
    >>> binary_search_iterative(names, 'Nick')
    '5'
    >>> binary_search_iterative(names, 'Brian')
    '1'
    Returns
    ----------
    Returns integer index of item.

    Time Complexity
    ---------------
    Best Case: Ω(1) target is middle index
    Average Case: O(log𝑛)
    Worst Case: Θ(log𝑛)
    """
    """ For the case of 1 read, the position should be in the middle so there is a probability of 1𝑛 for this case
        For the case of 2 reads, one will read the middle position and then 1 of the 2 other middle positions from the 2 sub-arrays. This probability is 2𝑛
        For the case of 3 reads, there are 2∗2 positions which result in this cost as you go into the 4 sub-arrays of the first 2 sub-arrays. The probability for this cost is 22𝑛
        ...

        For the case of 𝑥 reads, the probability for this case is 2𝑥−1𝑛
        For the average case, the number of reads will be

        ∑𝑖=1log(𝑛)𝑖2𝑖−1𝑛=1𝑛∑𝑖=1log(𝑛)𝑖2𝑖−1
        Now you can do integration on an approximation formula which will give you 𝑂(𝑛log(𝑛)). Note that ∫1log(𝑛)𝑥2𝑥𝑑𝑥 can be calculated and bounded into log(𝑛)∗2log(𝑛)=𝑛log(𝑛) This is a very good way to do that applies to many cases.

        Another way to see it can also be 𝑖2𝑖−1<log(𝑛)∗2𝑖−1
        Then the formula above is bounded by log(𝑛)𝑛∑𝑖=1log(𝑛)2𝑖−1
        The summation part is actually 1−2log(𝑛)1−2=2log(𝑛)−1=𝑛−1 which is definitely less than 𝑛, multiplying this with log(𝑛)𝑛 gives you what you want log(𝑛)
        So you will get the bound as you want  Θ(log(𝑛))
    """

    l = 0
    r = len(array) - 1
    bisect = 0

    while l <= r:
        # bisection or middle
        bisect = l + (r - l) // 2

        # Check if item  is present at mid
        if arr[bisect] == item:
            return bisect

        # If item is greater, ignore left half
        elif arr[bisect] < item:
            l = bisect + 1

        # If item is smaller, ignore right half
        else:
            r = bisect - 1

    # Not present
    return None


def binary_search_recursive(array, item):
    """
    names = ['Alex', 'Brian', 'Julia', 'Kojin', 'Nabil', 'Nick', 'Winnie']
    >>> binary_search_recursive(names, 'Alex')
    '0'
    >>> binary_search_recursive(names, 'Winnie')
    '6'
    >>> binary_search_recursive(names, 'Nick')
    '5'
    >>> binary_search_recursive(names, 'Brian')
    '1'
    Returns
    ----------
    Returns integer index of item.

    Time Complexity
    ---------------
    Best Case: Ω(1)
    Average Case: O(log𝑛)
    Worst Case: Θ(log𝑛)
    """
    """ For the case of 1 read, the position should be in the middle so there is a probability of 1𝑛 for this case
        For the case of 2 reads, one will read the middle position and then 1 of the 2 other middle positions from the 2 sub-arrays. This probability is 2𝑛
        For the case of 3 reads, there are 2∗2 positions which result in this cost as you go into the 4 sub-arrays of the first 2 sub-arrays. The probability for this cost is 2^2𝑛
        ...

        For the case of 𝑥 reads, the probability for this case is 2𝑥−1𝑛
        For the average case, the number of reads will be

        ∑𝑖=1log(𝑛)𝑖2𝑖−1𝑛=1𝑛∑𝑖=1log(𝑛)𝑖2𝑖−1
        Now you can do integration on an approximation formula which will give you 𝑂(𝑛log(𝑛)). Note that ∫1log(𝑛)𝑥2𝑥𝑑𝑥 can be calculated and bounded into log(𝑛)∗2log(𝑛)=𝑛log(𝑛) This is a very good way to do that applies to many cases.

        Another way to see it can also be 𝑖2𝑖−1<log(𝑛)∗2𝑖−1
        Then the formula above is bounded by log(𝑛)𝑛∑𝑖=1log(𝑛)2𝑖−1
        The summation part is actually 1−2log(𝑛)1−2=2log(𝑛)−1=𝑛−1 which is definitely less than 𝑛, multiplying this with log(𝑛)𝑛 gives you what you want log(𝑛)
        So you will get the bound as you want  Θ(log(𝑛))
    """
    l = 0  # left endpoint
    r = len(array) - 1  # right endpoint
    return whyAlan(array, item, l, r)


def whyAlan(array, item, l, r):
    # check case
    if l > r:
        return None

    # the midpoint or bisection
    bisect = (l + r) // 2
    # check side item should be on
    if array[bisect] < item:

        # Else the element can only be present in left subarray
        return whyAlan(array, item, bisect + 1, r)

    elif array[bisect] > item:
        # Else the element can only be present in right subarray
        return whyAlan(array, item, l, bisect - 1)
    else:
        # Check if item is present at middle
        return bisect
