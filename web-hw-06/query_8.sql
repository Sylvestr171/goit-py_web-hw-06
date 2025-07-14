--Знайти середній бал, який ставить певний викладач зі своїх предметів.
select subjects.name, AVG(grades.grade) 
from grades 
join subjects on grades.subject_id = subjects.id 
join teachers on subjects.teacher_id = teachers.id 
where teachers.fullname = %s group by subjects.name