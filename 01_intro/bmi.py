waga = float(input("Podaj wagę w kg: "))
wzrost = float(input("Podaj wzrost w m: "))
bmi = waga / wzrost ** 2

print("Moje BMI to: ", round(bmi, 2))
