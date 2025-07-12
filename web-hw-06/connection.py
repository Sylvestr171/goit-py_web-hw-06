import psycopg2
from contextlib import contextmanager

connection_params="host=localhost dbname=postgres user=postgres password=example"

@contextmanager
def create_connection(connect_params :str = "host=localhost dbname=postgres user=postgres password=example"):
    try:
        """ create a database connection to postgresql """
        conn = psycopg2.connect(connect_params)
        yield conn
        conn.close()
    except psycopg2.OperationalError as err:
        raise RuntimeError(f"Failed to create database connection {err}")
    
    if __name__ == '__main__':
        create_connection()