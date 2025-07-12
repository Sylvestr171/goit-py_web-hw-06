import logging
from psycopg2 import DatabaseError

from connection import create_connection, connection_params


def create_table(conn, sql_expression: str):
    """ create a table from the create_tables.sql statement
    :param sql_expression:
    :param conn: Connection object
    :return:
    """
    c = conn.cursor()
    try:
        c.execute(sql_expression)
        conn.commit()
    except DatabaseError as e:
        logging.error(e)
        conn.rollback()
    finally:
        c.close()

if __name__ == '__main__':

    with open("create_tables.sql", "r") as sql:
        sql_script = sql.read()
        
    statements = [stmt.strip() for stmt in sql_script.strip().split(';') if stmt.strip()]
    
    try:
        with create_connection(connection_params) as conn:
            if conn is not None:
                for _ in statements:
                    create_table(conn, _)
            else:
                print("Error! cannot create the database connection.")
    except RuntimeError as err:
        logging.error(err)

