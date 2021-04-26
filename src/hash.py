"""
Uso: Hash es una función que convierte una cadena de texto de cualquier longitud
Creador: Andrés Hernández Mata
Version: 1.0.0
Python: 3.9.1
Fecha: 26 Abril 2020
"""

import hashlib
import os
from datetime import datetime
import time
import logging
import sys

os.system("cls")

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
log = logging.FileHandler("hash.log")
log.setLevel(logging.DEBUG)
logger.addHandler(log)

try:
    while True:        
        ruta = input("Ruta del directorio > ")
        if ruta != '':
            break
        os.system("cls")
    logger.info(ruta)        
    for archivo in os.listdir(ruta):        
        file_obj = open(os.path.join(ruta,archivo),'rb')
        logger.info(archivo)
        file = file_obj.read()
        hash_file = hashlib.sha256(file) 
        hashed_file = hash_file.hexdigest()
        logger.info(hashed_file)
    print(datetime.now(), '\033[0;32m [INFO] Archivo generado (hash.log) \033[0;0m')
except Exception as error:
    print(datetime.now(), '\033[0;91m [ERROR] Ha ocurrido un error ')
    print(error)
except KeyboardInterrupt:
    print()
    print(datetime.now(), '\033[0;32m [INFO] Saliendo... \033[0;0m')
    sys.exit()

