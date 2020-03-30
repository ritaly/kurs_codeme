# 1. Funkcja pyta użytkowników o pary książka + ocena i zapisuje je w programie
# 2. Pyta o nr książki i wyświetli film wraz z oceną
# 3. Błąd - użytkownik pyta o numer w bazie którego nie ma

def add_books_to_library(book_number):
    books = []
    for k in range(book_number):
        title = input("Podaj tytul ksiazki: ")
        grade = int(input("Podaj ocene ksiazki 1-10: "))
        books.append((title, grade))
        print('----------------------------')

    return books

def show_book(books):
    """This method shows book by id"""
    nr = int(input("Podaj nr ksiazki do wyswietlenia:"))
    index = nr - 1
    if index >= len(books):
        print("Nie mam tyle książek")
    else:
        print(f"Twoja ksiazka to {books[index]}")


# counter = int(input("Ile książek chcesz dodać?"))
# library = add_books_to_library(counter)
# print(library)
# show_book(library)

print(show_book.__doc__)