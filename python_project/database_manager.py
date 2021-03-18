import pyodbc
import api_requests as api
from datetime import datetime, date


def opens_connection():
    try:
        return pyodbc.connect('Driver={SQL Server};'
                              'Server=nearestserver.database.windows.net;'
                              'Database=covid_schema;'
                              'UID=<MY_USER>;'
                              'PWD=<MY_PASSWORD>;',
                              autocommit=True)

    except Exception as e:
        print(f'Erro ao conectar no SQL Server no Azure.', e)


def opens_cursor():
    connection = opens_connection()
    return connection, connection.cursor()


def insert_data(cursor, table, data):
    pass


def data_manager():
    print('Testing API request service...')
    request_response = api.main_endpoint()
    print('API request established...')

    print('Testing database connection...')
    conn, temp_cursor = opens_cursor()
    print("Connection successfully established...")

    # insert_data(cursor, <SELECTED_TABLE>, <DATA>)

    temp_cursor.close()
    conn.close()


execution_start = datetime.now()
print('Starting script execution...')

print('Data manipulation started...')
data_manager()
print('Data manipulation completed...')

elapsed = datetime.now() - execution_start
print(f'Script execution finalized. Elapsed time: {elapsed}')
