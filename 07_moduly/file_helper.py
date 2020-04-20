# Stwórz moduł, który zajmuje się jedynie otwieraniem plików
# - oferuje bezpieczny sposób odczytu oraz bezpieczny zapis.
# unkcja czytająca pliki sprawdza najpierw czy dany plik istnieje
# oraz czy jest niepusty.
# Funkcja zapisująca do pliku chroni przed nadpisaniem istniejącego pliku.


def safe_open(file_name):
    with open(file_name) as f:
        content = f.read()
    return content


def safe_save(file_name, content):
    with open(file_name, 'x', encoding='utf-8') as f:
        f.write(content)
    print('Zapisano')