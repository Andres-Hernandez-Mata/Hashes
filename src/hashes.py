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

print(now, '\033[0;32m [INFO] Lista de algoritmos disponibles \033[0;0m')
time.sleep(1)
print(hashlib.algorithms_available)

texto = 'Hola'

print(now, '\033[0;32m [INFO] Texto \033[0;0m')
time.sleep(1)
print(texto)

md5_txt = hashlib.md5(texto.encode())
print(now, '\033[0;32m [INFO] Hash MD5 del Texto \033[0;0m')
time.sleep(1)
print(md5_txt.hexdigest())

sha1_txt = hashlib.sha1(texto.encode())
print(now, '\033[0;32m [INFO] Hash SHA-1 del Texto \033[0;0m')
time.sleep(1)
print(sha1_txt.hexdigest())

sha256_txt = hashlib.sha256(texto.encode())
print(now, '\033[0;32m [INFO] Hash SHA-256 del Texto \033[0;0m')
time.sleep(1)
print(sha256_txt.hexdigest())

sha512_txt = hashlib.sha512(texto.encode())
print(now, '\033[0;32m [INFO] Hash SHA-512 del Texto \033[0;0m')
time.sleep(1)
print(sha256_txt.hexdigest())

