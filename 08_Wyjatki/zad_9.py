import webbrowser

def check_sufix(url):
    allowed_suffixes = ('pl', 'com', 'fr')

    valid_url = False
    for sufix in allowed_suffixes:
        if url.endswith(sufix):
            print('Prawidlowa koncówka')
            valid_url = True
            break

    if not valid_url:
        raise TypeError('Twój url nie jest obsługiwany')

def with_prefix(url):
    if url.startswith('https://') or url.startswith('http://'):
        return url
    else:
        return 'http://' + url


# Prawidlowe urle:
    # https://flynerd.pl
    # http://flynerd.pl
    # www.flynerd.pl
    # flynerd.pl
    # https://www.flynerd.pl
    # http://www.flynerd.pl
    # https://flynerd.pl
    # https://flynerd.pl
#     1. mają odpowiednie koncowki
#     2. nie mają spacji

user_url = input('Podaj strone www')
user_url = user_url.strip()
user_url = user_url.replace(' ', '')

try:
    check_sufix(user_url)
except TypeError as e:
    print('Wpadł błąd')
    print(e)
else:
    webbrowser.open(with_prefix(user_url))
