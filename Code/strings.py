#!python


def contains(text, pattern):
    """
    Return a boolean indicating whether pattern occurs in text.

     Time Complexity
    ---------------
    Best: 
    Average: O(p * t) -- p being length of pattern and l being length of text
    Worse:
    """
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    return find_index(text, pattern) != None


def find_index(text, pattern):
    """
    Return the starting index of the first occurrence of pattern in text, or None if not found.
    Time Complexity
    ---------------
    Best: 
    Average: O(p * t) -- p being length of pattern and l being length of text
    Worse:
    """
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    # Edge case - this check makes the code O(p * n) instead of O(p^2 + n*p)
    if len(pattern) > len(text):
        return None

    # check if the pattern is an empty string and return 0 if so
    if pattern == '':
        return 0
    # loop through the text keeping the index and current character
    for i, character in enumerate(text):
        # check if the character is the same as the beginning of the pattern
        if character == pattern[0]:
            for j, character2 in enumerate(pattern):
                # current index of i + where we are on j
                curr_index = j + i
                # check bounds and letter
                if curr_index > len(text)-1 or text[curr_index] != character2:
                    break
            else:
                # if we do not break out we found the occurance
                return i
    # return None if no patterns match
    return None


def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found.
    Time Complexity: O(p * t) -- p being length of pattern and t being length of text
    """
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    # Edge case - this check makes the code O(p * n) instead of O(p^2 + n*p)
    if len(pattern) > len(text):
        return []

    # check if the pattern is an empty string and return a list of all the indexes if true
    if pattern == '':
        return [i for i in range(len(text))]

    # list of indexes to return
    indexes = []
    # loop through the text keeping the index and current character
    for i, character in enumerate(text):
        # check if the character is the same as the beginning of the pattern
        if character == pattern[0]:
            # check that if the characters starting at character to the length of the pattern is equal to the pattern
            for j, character2 in enumerate(pattern):
                # current index of i + where we are on j
                curr_index = j + i
                # check bounds and letter
                if curr_index > len(text)-1 or text[curr_index] != character2:
                    break
            else:
                # will only occur if loop is not broken out of
                indexes.append(i)
    # return the list of indexes
    return indexes
