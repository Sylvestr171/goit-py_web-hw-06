--Знайти середній бал у групах з певного предмета.
SELECT AVG(grades.grade) as avg_grade,groups.name, subjects.name 
FROM grades 
join students on grades.student_id = students.id 
join groups on students.group_id = groups.id 
join subjects on grades.subject_id = subjects.id 
where subjects.name = %s 
GROUP BY groups.name, grades.subject_id, subjects.name