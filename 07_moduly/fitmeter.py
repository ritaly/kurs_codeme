import bmi

w = float(input("Podaj wage [kg]:"))
h = float(input("Podaj wzrost [m]:"))

result_bmi = bmi.calculate_bmi(w, h)
state = bmi.get_state(result_bmi)
print(state)

filename = state.lower() + '.txt'
with open(filename) as fopen:
    tip = fopen.read()

print(tip)