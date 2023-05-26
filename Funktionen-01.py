
# -----------------------
#       Unpacking
# -----------------------
koordinate = (120, 40)

# So machen das viele andere Programmiersprachen

x = koordinate[0]
y = koordinate[1]

# So macht das Python = the pythonic Way

x, y = koordinate

# -----------------------
#       Swapping
# -----------------------
a = 10
b = 20

# So machen das viele andere Programmiersprachen

tmp = a
a = b
b = tmp
print(a, b)

# So macht das Python = the pythonic Way

a, b = b, a
print(a, b)

# -----------------------
#     True oder False
# -----------------------
liste = [0]

# So machen das viele andere Programmiersprachen

if len(liste) > 0:
    # mach irgendwas
    print(liste)

# So macht das Python = the pythonic Way

if liste:
    # mach irgendwas
    print(liste)

# -----------------------
#    Ternary Operator
# -----------------------
alter = 20

# So machen das viele andere Programmiersprachen

if alter > 17:
    erwachsen = True
else:
    erwachsen = False

# So macht das Python = the pythonic Way

erwachsen = True if alter > 17 else False

# -----------------------
#         Split
# -----------------------
# So machen das viele andere Programmiersprachen

rollen = ["Brian", "Stan", "Judith", "Pontius", "Centurio"]
print(rollen)

# So macht das Python = the pythonic Way

rollen2 = "Brian Stan Judith Pontius Centurio".split()  # (" ") oder ("u") ...
print(rollen2)

# -----------------------
#   List Comprehension
# -----------------------
# So machen das viele andere Programmiersprachen

# poker_card_deck =[]
# suits = ["Herz","Karo","Pik","Kreuz"]

# for suit in suits:
#    for value in range(2,15):
#       poker_card_deck.append((value,suit))

# So macht das Python = the pythonic Way

poker_card_deck = [(suit, value) for suit in "HKPK" for value in range(2, 15)]
print(poker_card_deck)

# -----------------------
#  Beliebige Genauigkeit
# -----------------------
# So machen das viele andere Programmiersprachen

print(f'{2**64-1:e}')

# So macht das Python = the pythonic Way

print(2**64-1)

# -------------------------------------------------------------
#  Element in iterable = (durchsuchbare Anzahlen von Elementen)
# -------------------------------------------------------------
liste2 = [1, 2, 3, 7]

# So machen das viele andere Programmiersprachen

for element in liste2:
    if element == 5:
        print(element, "ist enthalten")

# So macht das Python = the pythonic Way

if 7 in liste2:
    print("ist enthalten")

# Das funktioniert mit Dictionarys, Sets, Strings

if "o" in "Hannover":
    print("ist enthalten")

# -----------------------
#     Letztes Element
# -----------------------
liste3 = [1, 2, 3, 7]

# So machen das viele andere Programmiersprachen

print(liste3[len(liste3)-1])

# So macht das Python = the pythonic Way

print(liste3[-1])

# -----------------------
#    For Item in List
# -----------------------
liste4 = [1, 2, 3, 4, 9, 18, 99, 23]

# So machen das viele andere Programmiersprachen

for i in range (0,len(liste4)):
    print(liste4[i])
    
# So macht das Python = the pythonic Way

for element in liste4:
    print(element)

