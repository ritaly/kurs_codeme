def is_card_number(number):
    return number.isdecimal() and len(number) in [13, 15, 16]

def starts_with_correct_digits(number):
    if 51 <= int(number[0:2]) <= 55:
        return True
    elif 2221 <= int(number[0:4]) <= 2720:
        return True
    else:
        return False

def show_card_type(number):
    if len(number) in [13, 16] and number[0] == '4':
        print("To jest Visa")

    elif len(number) == 16 and starts_with_correct_digits(number):
        print("To jest MasterCard")

    elif len(number) == 15 and (number[0:2] in [ '34', '37']):
        print("To jest American Express")
    else:
        print("Nie znam typu karty")


nr_card = input('Podaj numer karty:')
nr_card = nr_card.replace(" ", "")
print("Podany numer to: ", nr_card)

if is_card_number(nr_card):
    show_card_type(nr_card)
else:
    print('to nie jest nr karty')