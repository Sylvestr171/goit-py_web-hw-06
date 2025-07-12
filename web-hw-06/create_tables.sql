-- Таблиця груп
CREATE TABLE if NOT EXISTS groups (
  id SERIAL PRIMARY KEY,
  name VARCHAR(50) NOT NULL
);

-- Таблиця студентів
CREATE TABLE if NOT EXISTS students (
  id SERIAL PRIMARY KEY,
  fullname VARCHAR(150) NOT NULL,
  group_id INTEGER REFERENCES groups(id)
  	on delete cascade
);

-- Таблиця викладачів
CREATE TABLE if NOT exists teachers (
  id SERIAL PRIMARY KEY,
  fullname VARCHAR(150) NOT NULL,
  email VARCHAR(150)
);

-- Таблиця предметів
CREATE TABLE if NOT exists subjects (
  id SERIAL PRIMARY KEY,
  name VARCHAR(175) NOT NULL,
  teacher_id INTEGER  REFERENCES teachers(id)
  	on delete cascade
);

-- Таблиця оцінок
CREATE TABLE if NOT EXISTS grades (
  id SERIAL PRIMARY KEY,
  student_id INTEGER  REFERENCES students(id)
  on delete cascade,
  subject_id INTEGER  REFERENCES subjects(id)
  on delete cascade,
  grade INTEGER CHECK (grade >= 0 AND grade <= 100),
  grade_date DATE NOT NULL
);
