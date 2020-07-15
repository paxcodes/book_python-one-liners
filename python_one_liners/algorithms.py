def is_anagram(string1, string2):
    """Angrams consist of the same characters and if every character of the
    1st word appears in the 2nd word exactly once."""
    return sorted(string1) == sorted(string2)


def is_anagram_through_histogramming(string1, string2):
    """Angrams consist of the same characters and if every character of the
    1st word appears in the 2nd word exactly once.

    Histogramming counts the number of occurrences of all characters in that
    string, and then compare the two histograms."""
    histogram1 = {}
    for char in string1:
        histogram1[char] = histogram1.get(char, 1)

    histogram2 = {}
    for char in string2:
        histogram2[char] = histogram2.get(char, 1)

    return histogram1 == histogram2


def is_palindrome(word):
    return word == word[::-1]


def get_factorial(num):
    factorial = 1
    while num > 1:
        factorial *= num
        num -= 1
    return factorial
    # return 1 if num <= 1 else get_factorial(num - 1) * num
