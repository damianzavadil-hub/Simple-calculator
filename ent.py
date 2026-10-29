# Kalkulačka

calc_input = input("Vyplňte výpočet s hodnotami ve tvaru x op y: ")

vstup = calc_input.replace(" ", "")

#  op = operátor
# Podporované operace:
#    + sčítání
#    - odčítání
#    * násobení
#    / dělení
#    ^ mocnina

if "+" in vstup:
    parts = vstup.split("+")
    a = int(parts[0])
    b = int(parts[1])
    calc_output = a + b

elif "-" in vstup:
    parts = vstup.split("-")
    a = int(parts[0])
    b = int(parts[1])
    calc_output = a - b

elif "*" in vstup:
    parts = vstup.split("*")
    a = int(parts[0])
    b = int(parts[1])
    calc_output = a * b

elif "/" in vstup:
    parts = vstup.split("/")
    a = int(parts[0])
    b = int(parts[1])
    if b == 0:
        calc_output = "Dělení nulou není povoleno!"
    else:
        calc_output = a / b

elif "^" in vstup:
    parts = vstup.split("^")
    a = int(parts[0])
    b = int(parts[1])
    calc_output = a ** b
else:
    calc_output = "Byl obdržen neplatný vstup!"

print(calc_input, "=", calc_output)
