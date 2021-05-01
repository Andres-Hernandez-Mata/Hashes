"""
Uso: Hashes y tablas arcoíris
Creador: Andrés Hernández Mata
Version: 1.0.0
Python: 3.9.1
Fecha: 27 Abril 2020
"""

import hashlib
from datetime import datetime

def arcoiris_md5():
    try:
        with open('arcoiris_md5.txt', 'w') as tabla_md5:
            for password in open("100passwords.txt").read().split():
                hash_md5 = hashlib.md5(password.encode())
                tabla_md5.write(hash_md5.hexdigest() + ': ' + password + '\n')
            print(datetime.now(), '\033[0;32m [INFO] Generando (arcoiris_md5.txt) \033[0;0m')
    except Exception as error:
        print(datetime.now(), '\033[0;91m [ERROR] Ha ocurrido un error ')
        print(error)

def arcoiris_sha256():
    try:
        with open('arcoiris_sha256.txt', 'w') as tabla_sha256:
            for password in open("100passwords.txt").read().split():
                hashes_sha_256 = hashlib.sha256(password.encode())
                tabla_sha256.write(hashes_sha_256.hexdigest() + ': ' + password + '\n')
            print(datetime.now(), '\033[0;32m [INFO] Generando (arcoiris_sha256.txt) \033[0;0m')
    except Exception as error:
        print(datetime.now(), '\033[0;91m [ERROR] Ha ocurrido un error ')
        print(error)


if __name__ == '__main__':
    arcoiris_md5()
    arcoiris_sha256()    