
# Returnerar det näst största talet i listan
# Returnerar None om det inte finns något
# Om det är delad första plats så returneras det talet.

from ..src.uppgift_2_5 import find_2nd_max

def test__find_2nd_max__returns_2nd_max():
    testdata = [1,3,2,4]
    expected = 3
    actual == find_2nd_max(testdata)
    assert actual == expected

def test__find_2nd_max__None_when_no_2nd_max():
    testdata = []
    expected = None
    actual == find_2nd_max(testdata)
    assert actual == expected

    assert find_2nd_max([11]) == None