--Знайти список курсів, які відвідує студент.
select subjects.name 
from subjects 
join grades on grades.subject_id = subjects.id 
join students on grades.student_id = students.id 
where students.fullname = %s group by subjects.name