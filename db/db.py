import psycopg2
from core import settings


def db_connection(db_name=settings.connection_data['db_name'], db_user=settings.connection_data['db_user'],
                  db_password=settings.connection_data['db_password'],
                  db_host=settings.connection_data['db_host'], db_port=settings.connection_data['db_port']):
    try:

        connection = psycopg2.connect(
            database=db_name, user=db_user, password=db_password, host=db_host, port=db_port
        )

    except ConnectionError as e:
        raise ConnectionError(f"DataBase connection Error:{e}")

    return connection
