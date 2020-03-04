palindrom = "Kobyła ma mały bok"
palindrom = palindrom.replace(" ", "")
palindrom = palindrom.lower()
print(palindrom)
print(palindrom == palindrom[::-1])