
from src.uppgift_2_1 import c_to_f
def test_c_to_f__temp_returns_zero():
    expected = 32
    actual = c_to_f(0)
    assert expected == actual