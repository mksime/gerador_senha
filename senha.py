import string
import random

sinais = string.punctuation
maiusculas = string.ascii_uppercase
minusculas = string.ascii_lowercase
numeros = string.digits

for i in sinais:
    if i in r"'\\/_=^`\|~\"":
        sinais = sinais.replace(i, "")

total = sinais + maiusculas + minusculas + numeros

while True:
    senha = ""
    sinal = False
    maiuscula = False
    minuscula = False
    numero = False
    for i in range(8):
        senha += random.choice(total)
    
    for char in senha:
        if char in sinais:
            sinal = True
        elif char in maiusculas:
            maiuscula = True
        elif char in minusculas:
            minuscula = True
        elif char in numeros:
            numero = True

    if sinal == True and maiuscula == True and minuscula == True and numero == True:
        break

print(senha)