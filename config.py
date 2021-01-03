import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'my-zoo-server.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'zoo-db'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'abuibaid'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or '[SQL_PASSWORD_GOES_HERE]'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'myzooblobstorage'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'uj5mO1niE89ZVHTNw5cx/cPHYap4IOHk3fu6dvQmbUzxqq+gRAz9w76/v/ErKj5uhW52IPedfT1Tk1TxHDKFjw=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'
