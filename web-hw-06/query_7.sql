--Знайти оцінки студентів у окремій групі з певного предмета.
SELECT students.fullname, grades.grade 
from grades 
join students on grades.student_id = students.id 
join groups on groups.id = students.group_id 
join subjects on grades.subject_id = subjects.id 
where groups.name = %s and subjects.name = %s