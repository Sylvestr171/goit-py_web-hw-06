--Знайти середній бал на потоці (по всій таблиці оцінок).
select groups.name, AVG(grades.grade)
from grades
join students on grades.student_id = students.id
join groups on students.group_id = groups.id
group by students.group_id, groups.name