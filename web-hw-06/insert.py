import logging
from random import randint, choice, sample

from faker import Faker
from psycopg2 import DatabaseError

from connection import create_connection, connection_params

number_of_students = randint(30,50)
number_of_groups = 3
number_of_subjects = randint(5,8)
number_of_teachers = randint(3,5)
# до 20 оцінок у кожного студента з усіх предметів

fake = Faker('uk-Ua')

class RandomNamedFromVocabulary():
    def __init__(self):
        self.name = self.generate_name()

    def generate_name(self):
        raise NotImplementedError("Цей метод має бути перевизначений у підкласі")

    def __str__(self):
        return self.name

class Group(RandomNamedFromVocabulary):
    faculties = ["ІХФ", "ПБФ", "РТФ", "ФМФ", "ФІОТ", "ФБІ", "ФЕА", "ФЕЛ", "ФЛ", "ФММ", "ФПМ", "XТФ"]

    def __init__(self):
        self.name = self.generate_name()

    def generate_name(self):
        faculty = choice(self.faculties)
        year = randint(22, 25)
        return f"{faculty}-{year}"

    def __str__(self):
        return self.name
    
class Subject(RandomNamedFromVocabulary):
    subjects_vocabulary = (
    "Вища математика",
    "Фізика",
    "Електротехніка",
    "Програмування",
    "Алгоритми та структури даних",
    "Системне програмування",
    "Математична логіка",
    "Теорія ймовірностей",
    "Комп’ютерна графіка",
    "Бази даних",
    "Мережі та телекомунікації",
    "Операційні системи",
    "Архітектура комп’ютерів",
    "Штучний інтелект",
    "Системи керування",
    "Моделювання систем",
    "Інформаційна безпека",
    "Сигнальні технології",
    "Мікроконтролери",
    "Проєктування цифрових схем"
)

    def __init__(self):
        self.name = self.generate_name()

    def generate_name(self):
        subject = choice(self.subjects_vocabulary)
        return f"{subject}"

    def __str__(self):
        return self.name

class People():
    def __init__(self):
        self.name = fake.name()

    def __str__(self):
        return self.name

class Teachers(People):
    def __init__(self):
        super().__init__()
        self.email = fake.email()

    def __str__(self):
        return f"{self.name} ({self.email})"
    
class Students(People):
    def __init__(self):
        super().__init__()

def insert_data(conn, sql_expression: str, data_to_insert: list, attr_list: list):
    c = conn.cursor()
    try:
        for i in data_to_insert:
            attribute = values = tuple(getattr(i, attr) for attr in attr_list)
            c.execute(sql_expression, attribute)
        conn.commit()
    except DatabaseError as e:
        logging.error(e)
        conn.rollback()
    finally:
        c.close()


if __name__ == '__main__':
    
    sql_insert_data_groups = """
        INSERT INTO groups (name) VALUES (%s);
        """
    
    sql_insert_data_students = """
        INSERT INTO students (fullname, group_id) VALUES (%s, (SELECT id FROM "groups" ORDER BY random() LIMIT 1));
        """
        
    sql_insert_data_teachers = """
        INSERT INTO teachers (fullname, email) VALUES (%s, %s);
        """
    
    sql_insert_data_subjects = """
        INSERT INTO subjects (name, teacher_id) VALUES (%s, (SELECT id FROM "teachers" ORDER BY random() LIMIT 1));
        """

    groups = [Group() for _ in range(number_of_groups)]
    students = [Students() for _ in range(number_of_students)]
    teachers = [Teachers() for _ in range(number_of_teachers)]
    subjects = []
    subjects = [Subject() for _ in range(number_of_subjects) if _ not in subjects]

    try:
        with create_connection() as conn:
            if conn is not None:
                insert_data(conn, sql_insert_data_groups, groups, ['name'])
                insert_data(conn, sql_insert_data_students, students, ['name'])
                insert_data(conn, sql_insert_data_teachers, teachers, ['name', 'email'])
                insert_data(conn, sql_insert_data_subjects, subjects, ['name'])
            else:
                print("Error! cannot create the database connection.")
    except RuntimeError as err:
        logging.error(err)