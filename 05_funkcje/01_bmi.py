# Skorzystaj ze swojego kodu bmi.py. Rozbij liczenie bmi na funkcję obliczającą
# bmi na podstawie danych użytkownika oraz zwracającą odpowiednią wartość
# (niedowaga, waga normalna, nadwaga, otyłość) w zależności od otrzymanego parametru.

# funkcja obliczająca BMI <- waga, wzrost
def calculate_bmi(weight, height):
    return weight /height ** 2

# funkcja podająca wartość
def get_state(bmi):
    if bmi < 18:
        print("Niedowaga")
    elif bmi < 25:
        print("Waga normalna")
    elif bmi < 30:
        print("Nadwaga")
    else:
        print("Otyłość")


# reszta kodu
# podaj wage i wzrost
w = float(input("Podaj wage [kg]:"))
h = float(input("Podaj wzrost [m]:"))

result_bmi = calculate_bmi(w, h)
get_state(result_bmi)