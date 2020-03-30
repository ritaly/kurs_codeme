
people = [
    ["Dorota", "Wellman", "dziennikarka"],
    ["Adam", "Małysz", "sportowiec"],
    ["Robert", "Lewandowski", "piłkarz"],
    ["Krystyna", "Janda", "aktorka"]
]


for row in people:
    #print(f"{row[0]} {row[1]} - {row[2]}")
    name = " ".join(row[:2])
    print(name + " - " + row[2])