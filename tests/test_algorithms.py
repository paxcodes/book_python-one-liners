from python_one_liners import algorithms as al


def test_anagrams():
    assert al.is_anagram("elvis", "lives")
    assert al.is_anagram("elvise", "livees")
    assert not al.is_anagram("elvise", "dead")


def test_anagrams_using_histograms():
    assert al.is_anagram_through_histogramming("elvis", "lives")
    assert al.is_anagram_through_histogramming("elvise", "livees")
    assert not al.is_anagram_through_histogramming("elvise", "dead")
