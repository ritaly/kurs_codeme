l_per_100 = float(input("Podaj spalanie na 100km: "))
distance = int(input("Jak daleko jedziemy? "))
price_per_l = 5.04

total = price_per_l * distance/100 * l_per_100

print(round(total, 2))