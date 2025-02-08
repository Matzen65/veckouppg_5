from src.example import subtract

def test_subtract__subtracts_correctly():
    #x = 10
    #y = 7
    expected = 3
    actual = subtract(10, 7)
    assert actual == expected