import os


'''
*
Файл с переменными окружения
*
'''


DBUSER = os.environ.get('DBUSER')
DBHOST = os.environ.get('DBHOST')
DBNAME = os.environ.get('DBNAME')
DBPORT = os.environ.get('DBPORT')
DBPASSWORD = os.environ.get('DBPASSWORD')
TOKEN = os.environ.get('TOKEN')
EADRESS = os.environ.get('EADRESS')
EPASSWORD = os.environ.get('EPASSWORD')
DEBUG = os.environ.get('DEBUG') or False
RESTIP = os.environ.get('RESTIP') or 'localhost'
RESTPORT = os.environ.get('RESTPORT') or '8000'