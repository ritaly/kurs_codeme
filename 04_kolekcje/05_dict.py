"""Szybko, zbudź się, szybko, wstawaj
Szybko, szybko, stygnie kawa
Szybko, zęby myj i ręce"""

# W wierszu policz wystąpienie każdego wyrazu, zignoruj wielkość liter.

poem = """Szybko, zbudź się, szybko, wstawaj
Szybko, szybko, stygnie kawa, kawa
Szybko, zęby myj i ręce"""

poem = poem.lower()
poem = poem.replace(",", "")
word_list = poem.split()

words_in_poem = {}

for w in word_list:
    if w in words_in_poem:
        words_in_poem[w] += 1
    else:
        words_in_poem[w] = 1

for word, number in words_in_poem.items():
    print(f"* {word} : {number}")