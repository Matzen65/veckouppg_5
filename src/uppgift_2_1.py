# 2 Öva på TDD
# Samla ihop dina funktioner så att de ligger i en eller flera moduler. Importera och anropa dem från main.py, så att main-filen bara innehåller funktionsanrop.

# 1a Hitta på lämplig testdata till följande funktion, som omvandlar grader Celsius till grader Fahrenheit.
# svar 1a: C_to_F(-275)(expected None), C_to_F(10) (expected 50),  C_to_F(70) expected = 158
def c_to_f(degree):
    if degree < -273.15:
        return None
    return degree * 9 / 5 + 32



# 1b Vilka ekvivalensklasser har parametern degree?
# svar 1b: Flyttal större än eller lika med -273.15.

# 1c Skriv ett testfall.
# svar 1c: test_uppgift_2_1.py




"""
from src.uppgift_2_1 import c_to_f
def test_c_to_f__temp_returns_zero():
    expected = 32
    actual = c_to_f(0)
    assert expected == actual

from src.uppgift_2_1 import c_to_f
def test_c_to_f__low_returns_none():
    expected = None
    actual = c_to_f(-275)
    assert expected == actual
"""