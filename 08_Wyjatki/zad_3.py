import sys
my_list = [3, '345', {'a': 1}, 0, ['d', 'a']]

try:
    index = float(input('Podaj index:'))
    wynik = my_list[1/index]
except (TypeError, ValueError) as message:
    print('Exception message: ', message)
else:
    print(wynik)