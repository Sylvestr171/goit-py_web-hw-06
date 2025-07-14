--Список курсів, які певному студенту читає певний викладач.
select subjects.name 
from subjects 
join grades on grades.subject_id = subjects.id 
join students on grades.student_id = students.id 
join teachers on teachers.id = subjects.teacher_id 
where students.fullname = %s
and teachers.fullname = %s 
group by subjects.name