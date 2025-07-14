import logging
from psycopg2 import DatabaseError
from connection import create_connection, connection_params

if __name__ == '__main__':
    sql_expression_01 = """
        SELECT * FROM users WHERE id = %s;    
        """
    
    sql_scripts = {}

    for i in range(1,11):
        with open(f"web-hw-06\\query_{i}.sql", "r") as sql:
            sql_scripts[f"sql_script_{i}"] = sql.read()

    try:
        with create_connection(connection_params) as conn:
            if conn is not None:
                c = conn.cursor()
                try:
                    c.execute(sql_scripts["sql_script_1"])
                    result = c.fetchall()
                    print(f"query_1\n")
                    print(f"{result}\n")
                    c.execute(sql_scripts["sql_script_2"], (2,))
                    result = c.fetchall()
                    print(f"query_2\n")
                    print(f"{result}\n")
                    c.execute(sql_scripts["sql_script_3"], ("Вища математика",))
                    result = c.fetchall()
                    print(f"query_3\n")
                    print(f"{result}\n")
                    c.execute(sql_scripts["sql_script_4"])
                    result = c.fetchall()
                    print(f"query_4\n")
                    print(f"{result}\n")
                    c.execute(sql_scripts["sql_script_5"], ('Герман Салій',))
                    result = c.fetchall()
                    print(f"query_5\n")
                    print(f"{result}\n")
                    c.execute(sql_scripts["sql_script_6"], ('ІХФ-25',))
                    result = c.fetchall()
                    print(f"query_6\n")
                    print(f"{result}\n")
                    c.execute(sql_scripts["sql_script_7"], ('ІХФ-25','Вища математика'))
                    result = c.fetchall()
                    print(f"query_7\n")
                    print(f"{result}\n")
                    c.execute(sql_scripts["sql_script_8"], ('Ігнат Атаманюк',))
                    result = c.fetchall()
                    print(f"query_8\n")
                    print(f"{result}\n")
                    c.execute(sql_scripts["sql_script_9"], ('Джунь Августин Несторович',))
                    result = c.fetchall()
                    print(f"query_9\n")
                    print(f"{result}\n")
                    c.execute(sql_scripts["sql_script_10"], ('Джунь Августин Несторович','Герман Салій'))
                    result = c.fetchall()
                    print(f"query_10\n")
                    print(f"{result}\n")
                except DatabaseError as e:
                    logging.error(e)
                finally:
                        c.close()
            else:
                print("Error! cannot create the database connection.")
    except RuntimeError as err:
        logging.error(err)
