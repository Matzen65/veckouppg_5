# Uppgift 2.2, count_words(sentence)

from src.uppgift_2_2 import count_words

def test_count_words__empty_input():
    expected = 0
    assert count_words("") == expected

def test_count_words__not_a_string():
    expected = 0
    assert count_words(0) == expected
    assert count_words(0.0) == expected
    assert count_words(None) == expected

def test_count_words__three_words():
    expected = 3
    assert count_words("två vanliga ord") == expected

def test_count_words__five_words():
    expected = 5
    assert count_words("Vi testar med fem ord") == expected