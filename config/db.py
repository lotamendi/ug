import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Se deben instalar los paquetes para trabajar con este driver
# pip install mysql-connector
# pip install mysql
MYSQL = {
    'default' : {
        'ENGINE' : 'django.db.backends.mysql',
        'NAME' : 'posgrado',
        'USER' : 'root',
        'PASSWORD' : '',
        'HOST' : '127.0.0.1',
        'PORT' : '3306',
        'OPTIONS' : {
            'init_command' : "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }

}