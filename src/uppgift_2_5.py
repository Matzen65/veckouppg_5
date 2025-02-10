# 5 Winner takes it all brukar det ju heta, men nu ska vi försöka ge lite heder åt alla andrapristagare.
# Formulera testfall för en funktion som hittar näst största talet i en lista

def find_2nd_max(list):
    if len(list) < 2:
        return None
    new_list = list.copy()
    new_list.sort()
    next_largest = new_list[-2]
    return next_largest
