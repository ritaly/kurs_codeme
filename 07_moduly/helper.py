PI = 3.14

def count_A(seq):
    '''Method returns how many A letter are in string'''
    counter = 0
    for l in seq:
        if l.lower() == 'a':
            counter += 1
    return counter


def count_letter(seq):
    return len(seq)


def main():
    # reszta kodu

    word = 'Abracadabra'
    word2 = 'Hocuspockus'

    print(count_A(word))
    print(count_A(word2))


if __name__ == '__main__':
    print('Uruchomiony jako główny plik')
    main()
else:
    print('Urchomiono plik jako moduł')