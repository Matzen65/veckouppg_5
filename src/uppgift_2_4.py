# 4 Betrakta funktionen is_sorted_ascending(numbers). Den ska returnera True om
# listan numbers är sorterad i stigande ordning, False annars.

# 4a Vilka ekvivalensklasser har numbers?
# Svar 4a:

# 4b Formulera krav och acceptanskriterier för funktionen.
# Svar 4b:
# Returnerar False om listan inte är sorterad.
# Returnerar True om listan är sorterad.

# 4c Skriv testfall för funktionen.

def is_sorted_ascending(numbers):
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            return False
    return True
