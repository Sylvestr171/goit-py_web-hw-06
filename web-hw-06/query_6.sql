--Знайти список студентів у певній групі.
SELECT students.fullname
from students
join groups on students.group_id = groups.id
where groups.name = 'ІХФ-25'