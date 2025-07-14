--Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
SELECT AVG(grades.grade) as avarage_grades, students.fullname 
FROM grades 
JOIN students ON students.id=grades.student_id 
GROUP BY grades.student_id, students.fullname 
order by avarage_grades desc limit 5