# Stwórz skrypt, który przyjmuje
# 3 opinie użytkownika o książce.
# Oblicz średnią opinię o książce.
# W zależności od wyniku dodaj komunikaty.
# Jeśli uzytkownik ocenił książkę na ponad
# 7 - bardzo dobry,
# 5-7 przeciętna,
# 4 i mniej - nie warta uwagi.

x = int(input("Podaj ocenę 1-10: "))
y = int(input("Podaj ocenę 1-10: "))
z = int(input("Podaj ocenę 1-10: "))

avg = (x + y + z) / 3

print(avg)

if avg > 7:
    print("Bardzo dobry")
elif avg >= 5:
    print("Przecietny")
else:
    print("Nie warty uwagi")

