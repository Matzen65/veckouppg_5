
# Uppgift1
# Skriv ner vad du tror kommer skrivas ut.
# Skriv sedan in koden i din IDE, exakt som den står, och kör den.
# Fick du samma resultat som du trodde? Om inte, varför?

# 1 Vilka ekvivalensklasser har uttrycken?

#### 1a. x > 100

# Svar 1a.
# Visar True om 'x' Är en int eller float som är större än 100,även flyttal
# Visar False om 'x' Är int eller float som är lika med 100 eller mindre.

#### 1b. y == 42
# Visar True om 'y' Är int eller float som är lika med 42
# Visar False om 'y' Är int eller float som inte är lika 42.

####1c. len(text) >= 5
# Visar True om 'text' Alla strängar av längden 5 eller längre.
# Visar False om 'text' Om strängen har en längd som är under 5.

#### 1d.  z == True
# Visar True om 'z' boolean uttrycket är True.
# Visar False om 'z' boolean uttrycket är False

#### 1e. 8 < v < 16
# Visar True om 'v' Är int eller float är större än 8 samt mindre än 16.
# Visar False om 'v' Är int eller float är lika med 8 eller mindre eller 16 eller större.
# Booleska uttryck och ger också False.

#### 1f. w == 32 or w == 64 or w == 128
# Visar True om 'w' Är lika med ett int eller float som antar värdena 32, 64 eller 128.
# Visar False om 'w' Är andra värden.

#### 1g. if x < 5:  elif x < 10:  elif x < 15:  else
# Visar True för x < 5 Visar True om 'x' är Int eller float som är strikt mindre än 5.
# Visar True för x < 10 visar True om 'x' är Int eller float, lika med 5 eller större och mindre än 10.
# Visar True för x < 15 visar True om 'x' är Int eller float, lika med 10 eller större och mindre än 15.
# Villkoret för att uppfylla else är Int eller float, lika med 15 eller större.



# 2 Det har smugit sig in kommentarer i stället för kod på några ställen.
# Skriv färdigt testfallen test_empty_list och test_number_list.

# Returnerar summan av alla tal i listan
def sum_list(list):
    return None

def test_empty_list():
    expected = 0
    actual = sum_list([])
    assert actual == expected

def test_number_list():
    assert sum_list([5]) == 5
    assert sum_list([1,2,3,4]) == 10
    assert sum_list([-1, 2, -3, 4]) == 3
    assert sum_list([1, 2, 7, 4]) == 14

# 3a Diskutera följande kod, räcker det med ett testfall för att testa funktionen?

# Returnerar ett heltal med antalet vokaler som finns i ordet (aeiouyåäö)
def count_vowels(word):
    return None

def test_no_vowels():
    assert count_vowels("qwrt") == 0
    assert count_vowels("Tt") == 0
    assert count_vowels("123 123") == 0
    assert count_vowels("") == 0

# Assert kommandona funkar men syns inte utfallet för "de andra" assert testerna.


# 3b Skriv färdigt funktionen count_vowels med hjälp av TDD-metoden, red → green → refactor.

# Returnerar ett heltal med antalet vokaler som finns i ordet (aeiouyåäö)
def count_vowels(word):
    return 0

def test_no_vowels():
    assert count_vowels("qwrt") == 0
    assert count_vowels("Tt") == 0
    assert count_vowels("123 123") == 0
    assert count_vowels("") == 0

# Testet returnerar 0 då testet går igenom.
# Man får sedan skriva tillräckligt med tester för refactor


# 4 Formulera testfall för en funktion som hittar största talet i en lista.

# Returnera det största talet i listan
# Returnera None om det inte finns något
def find_max(list):
    None

def test_find_biggest_number_list():
    excepted = 38
    actual = find_max([16, 38, 1])
    assert actual == excepted

def test_find_biggest_number_list_show_none_when_empty():
    excepted = None
    actual = find_max([])
    assert actual == excepted

