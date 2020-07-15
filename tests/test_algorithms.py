from python_one_liners import algorithms as al


def test_anagrams():
    assert al.is_anagram("elvis", "lives")
    assert al.is_anagram("elvise", "livees")
    assert not al.is_anagram("elvise", "dead")


def test_anagrams_using_histograms():
    assert al.is_anagram_through_histogramming("elvis", "lives")
    assert al.is_anagram_through_histogramming("elvise", "livees")
    assert not al.is_anagram_through_histogramming("elvise", "dead")


def test_palindrome():
    assert al.is_palindrome("anna")
    assert not al.is_palindrome("kdljfasfjf")
    assert al.is_palindrome("rats live on no evil star")


def test_permutations_factorial():
    assert al.get_factorial(0) == 1
    assert al.get_factorial(1) == 1
    assert al.get_factorial(2) == 2
    assert al.get_factorial(3) == 6
    assert al.get_factorial(10) == 3628800


def test_levenshtein_distance():
    assert al.get_levenshtein_distance("cat", "chello") == 5
