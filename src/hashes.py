"""
Uso: Hash es una función que convierte una cadena de texto de cualquier longitud
Creador: Andrés Hernández Mata
Version: 1.0.0
Python: 3.9.1
Fecha: 24 Abril 2020
"""

import hashlib
import time
from datetime import datetime
import os

os.system('cls')

now = datetime.now()

print(now, '[INFO] Lista de algoritmos disponibles')
time.sleep(1)
print(hashlib.algorithms_available)

texto = 'Hola'

print(now, '[INFO] Texto')
time.sleep(1)
print(texto)

md5_txt = hashlib.md5(texto.encode())
print(now, '[INFO] Hash MD5 del texto')
time.sleep(1)
print(md5_txt.hexdigest())

