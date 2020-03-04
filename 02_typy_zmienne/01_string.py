text = input("Podaj tekst o dług. nieparzystej > 7:")
center = len(text)//2
new_text = text[center - 1] + text[center] + text[center + 1]

print(new_text)