import logging
from random import randint

from faker import Faker
from psycopg2 import DatabaseError

from connection import create_connection, connection_params

fake = Faker('uk-Ua')
COUNT = 30

def insert_data(conn, sql_expression: str):
    c = conn.cursor()
    try:
        for _ in range(COUNT):
            c.execute(sql_expression, (fake.name(), fake.email()))
        conn.commit()
    except DatabaseError as e:
        logging.error(e)
        conn.rollback()
    finally:
        c.close()


if __name__ == '__main__':
    sql_insert_data = """
        INSERT INTO teachers (fullname, email) VALUES (%s, %s);
        """

    try:
        with create_connection() as conn:
            if conn is not None:
                insert_data(conn, sql_insert_data)
            else:
                print("Error! cannot create the database connection.")
    except RuntimeError as err:
        logging.error(err)