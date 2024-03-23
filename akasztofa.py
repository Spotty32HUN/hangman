from random import choice
from os import system

HANGMANPICS = [r'''
  +---+
  |   |
      |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

filename = input("* Üdvözöllek az akasztófa játékban!\n---> Add meg a könyvtár nevét (kizárólag \".txt\"): ")
filename += ".txt"

try:
    with open(filename, encoding='utf-8') as f:
        szo = choice(f.readlines()).rstrip()
except:
    print(f"\n* Hiba történt a könyvtár megnyitásakor, alapértelmezett szavak használata engedélyezve.\n* Kérlek győződj meg, hogy a jelenlegi fájl egy helyen tartózkodik a \"{filename}\" fájlal és van tartalma.\n")
    szo = choice(["alma", "könyv", "banán", 
                  "egér", "tehén", "malac", 
                  "körte", "láda", "teve"])
    
del filename

szo_l = []

for x in szo:
    szo_l.append(x)

sikeres = []

for x in szo_l:
    sikeres.append('_')
    
print(HANGMANPICS[0])
print("\n")

print("Kész a szó, találd ki!\n")

elet = 6

print(*sikeres)
    
while sikeres != szo_l and elet != 0:
    talalat = input("\n> ")
    system("cls || clear")
    if talalat == szo:
        break
    for i in range(len(szo_l)):
        if talalat == szo_l[i]:
            sikeres[i] = talalat
    if not talalat in szo_l:
        elet -= 1
    match elet:
        case 6:
            print(HANGMANPICS[0])
        case 5:
            print(HANGMANPICS[1])
        case 4:
            print(HANGMANPICS[2])
        case 3:
            print(HANGMANPICS[3])
        case 2:
            print(HANGMANPICS[4])
        case 1:
            print(HANGMANPICS[5])
    print("\n")
    print(*sikeres)
    
if elet == 0:
    print(HANGMANPICS[6])
    print(f"Vesztettél! A szó: {szo}")
else:
    print(f"Nyertél! Hátralévő próbák: {elet}")
    
input()