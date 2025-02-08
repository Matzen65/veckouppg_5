
from src.uppgift_2_3 import find_median

def test_find_median__median_number():
    expected = 2
    assert find_median([1,2,1000]) == expected

def test_find_median__when_even_number_of_elements():
    expected = 300
    assert find_median([1,2,500,100,4,5]) == expected