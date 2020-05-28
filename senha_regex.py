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

codigo = re.compile(r'(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[!#$%&()*+,\-.:;<>?@\[\]{}])')
while True:
    senha = ""
    for i in range(8):
        senha += random.choice(total)
    
    verifica = codigo.search(senha)
    if verifica != None:
        print(senha)
        break

print(senha)
