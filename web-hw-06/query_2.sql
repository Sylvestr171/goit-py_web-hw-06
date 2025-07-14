--Знайти студента із найвищим середнім балом з певного предмета.
SELECT MAX(avg_grade), students.fullname
from (select AVG(grades.grade) as avg_grade
FROM grades
GROUP BY grades.subject_id, grades.student_id
), grades 
join students on grades.student_id=students.id
where grades.subject_id = 5
GROUP BY grades.subject_id, grades.student_id, students.fullname