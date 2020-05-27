#!/usr/bin/env python3
import string
import random
import re

sinais = string.punctuation
maiusculas = string.ascii_uppercase
minusculas = string.ascii_lowercase
numeros = string.digits

for i in sinais:
    if i in r"'\\/_=^`\|~\"":
        sinais = sinais.replace(i, "")

total = sinais + maiusculas + minusculas + numeros

codigo = re.compile(fr'(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[{{numeros}}])')
while True:
    senha = ""
    sinal = False
    maiuscula = False
    minuscula = False
    numero = False
    for i in range(8):
        senha += random.choice(total)
    
    verifica = codigo.search(senha)
    if verifica == None:
        print("deu merda")
        print(senha)
    else:
        print('yay')
        break


print(senha)
