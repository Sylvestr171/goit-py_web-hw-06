--Знайти які курси читає певний викладач.
SELECT subjects.name 
from teachers 
join subjects on teachers.id = subjects.teacher_id 
where teachers.fullname = %s