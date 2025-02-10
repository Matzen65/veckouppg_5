
from src.uppgift_2_4 import is_sorted_ascending

def test_is_sorted_ascending__not_sorted():
    expected = False
    assert is_sorted_ascending([1,7, 6, 8]) == expected

def test_is_sorted_ascending__sorted():
    expected = True
    assert is_sorted_ascending([1, 4, 5,7]) == expected
