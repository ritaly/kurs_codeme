# 1. tekst od uzytkownika
txt = input("Podaj dowolny tekst: ")

char_lower = 0
char_upper = 0
digits = 0
symbols = 0

# 2. pętla po tekscie
#dla każdego znaku

# 3. sprawdz czy:
#       czy mala litera?
#           dodaj + 1 do licznika malych liter
#       czy duza liter?
#           dodaj +1 do duzych
#       czy cyfra?
#           dodaj + 1 do cyfr
#       czy znak specjalny?
#           dodaj + 1 do znakow specjalnych
for l in txt:
    if l.islower():
        char_lower += 1

    if l.isupper():
        char_upper += 1

    if l.isdecimal():
        digits += 1

    if not l.isalnum():
        symbols += 1

print(f"Malych - {char_lower},",
      f"duzych - {char_upper}",
      f"cyfr - {digits}",
      f"symbole - {symbols}")

