lista_par = [
    ["dzien dobry", "bonjour"],
    ["ziemniaki", "pomme de terre"],
    ["dziekuje", "merci"]
]

slownik_fr = dict(lista_par)

print(slownik_fr)
print(slownik_fr['dziekuje'])

for k, v in slownik_fr.items():
    print(f"{k} - tłumaczenie: {v}")