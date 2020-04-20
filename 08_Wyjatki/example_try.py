# def rectangle(a, b):
#     return a * b
#
#
# try:
#     bok_a = int(input("Podaj bok A:"))
#     bok_b = int(input("Podaj bok_B:"))
#     #kod, który chcemy sprawdzić
# except Exception as wyjatek:
#     print("Błąd", wyjatek)
#     # kod, który wykonuję jeśli występuje błąd
# else:
#     print("Prawidłowe wartosci")
#     # kod, który wykonuje się jeśli błędu nie ma
#     print(rectangle(bok_a, bok_b))

# def nonsens_function():
#     user_data = input("Podaj jakas liczbe:")
#     x = -5 + float(user_data)
#     x = x + 'a'
#     result = 100 / x
#     return result
#
# try:
#     a = nonsens_function()
# except ZeroDivisionError:
#     print("wyjatek - wartosc 0")
# except TypeError as ex:
#     print("wyjatek - ", ex)
# except ValueError:
#     print("Wyjątek - value error")
# else:
#     print(a)

# try:
#     result = 8 + 9
# except TypeError:
#     print("Oh nie!")
# finally:
#     result = 0
#
# print(340 + result)

# import sys
#
# try:
#     100 / 0
# except Exception:
#     print("Wyjątek ->", sys.exc_info()[0])

file = open('example_exceptions.py')
content = file.readlines()
print(len(content))
raise ValueError("I'm rebel!")
print("Hallo")
file.close() # nie wykona się

