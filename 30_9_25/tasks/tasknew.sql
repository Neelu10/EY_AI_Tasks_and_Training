CREATE DATABASE UniversityDB;
USE UniversityDB;
-- Students Table
CREATE TABLE Students (
student_id INT PRIMARY KEY,
name VARCHAR(50),
city VARCHAR(50)
);
-- Courses Table
CREATE TABLE Courses (
course_id INT PRIMARY KEY,
course_name VARCHAR(50),
credits INT
);
-- Enrollments Table
CREATE TABLE Enrollments (
enroll_id INT PRIMARY KEY,
student_id INT,
course_id INT,
grade CHAR(2),
FOREIGN KEY (student_id) REFERENCES Students(student_id),
FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);
-- Insert Students
INSERT INTO Students VALUES
(1, 'Rahul', 'Mumbai'),
(2, 'Priya', 'Delhi'),
(3, 'Arjun', 'Bengaluru'),
(4, 'Neha', 'Hyderabad'),
(5, 'Vikram', 'Chennai');

INSERT INTO Courses VALUES
(101, 'Mathematics', 4),
(102, 'Computer Science', 3),
(103, 'Economics', 2),
(104, 'History', 3);
-- Insert Enrollments
INSERT INTO Enrollments VALUES
(1, 1, 101, 'A'),
(2, 1, 102, 'B'),
(3, 2, 103, 'A'),
(4, 3, 101, 'C'),
(5, 4, 102, 'B'),
(6, 5, 104, 'A');

-- level 1 ,task 1
DELIMITER $$
Create Procedure Getallstudents()
BEGIN
select student_id,name,city
from Students;
END $$

DELIMITER ;

call Getallstudents()
-- level 2 task 2
DELIMITER $$
Create Procedure Getallcourses()
BEGIN
select course_id,course_name,credits
from Courses;
END $$

DELIMITER ;
call Getallcourses()

-- task 3 level 1
DELIMITER $$
CREATE PROCEDURE FindStudentsByCity(IN city_name VARCHAR(50))
BEGIN
    SELECT * FROM Students WHERE city = city_name;
END $$
DELIMITER ;

call FindStudentsByCity('delhi')

-- task 1 level 2
DELIMITER $$
Create procedure liststudentswithcourses()
Begin
select s.student_id,s.name,c.course_name
from Students s
join Enrollments e on s.student_id=e.student_id
join courses c on e.course_id=c.course_id;
end $$
DELIMITER ;

call liststudentswithcourses();

-- task 2 level 2

DELIMITER $$
create procedure liststudentswithenrolledcourses(IN course_id INT)
BEGIN
select s.student_id,s.name
 from Students s
 join Enrollments e on s.student_id=e.student_id
  where e.course_id=course_id;
  END $$
DELIMITER ;

CALL liststudentswithenrolledcourses(102)

-- task 3 level 2
DELIMITER $$
create procedure countofstudent1()
BEGIN
select c.course_name,count(e.student_id) as student_count
from Courses c
left join Enrollments e on c.course_id=e.course_id
group by c.course_id ;
END $$
DELIMITER ; 

call countofstudent1();

-- task 1 level 3
DELIMITER $$
create procedure liststudentswithgrade()
BEGIN
select s.student_id,s.name,c.course_id,e.grade
from Students s
join Enrollments e on s.student_id=e.student_id
join courses c on e.course_id=c.course_id;
end $$
DELIMITER ;
call liststudentswithgrade()

DELIMITER $$
create procedure liststudentswithallcourse(IN student_id INT)
BEGIN
select c.course_name
 from Courses c
 join Enrollments e on c.course_id=e.course_id
where e.student_id=student_id;
  END $$
DELIMITER ;

call liststudentswithallcourse(2);

DELIMITER $$
CREATE PROCEDURE CoursesByStudent3()
BEGIN
    SELECT c.course_name, count(e.grade) as average_of_grade
    FROM Courses c
    JOIN Enrollments e ON c.course_id = e.course_id
    group by c.course_id;
END $$
DELIMITER ;

call CoursesByStudent3()

DELIMITER $$
CREATE PROCEDURE CoursesByStudent3()
BEGIN
    SELECT c.course_name, count( e.grade ) as average_of_grade
    FROM Courses 
    JOIN Enrollments e ON c.course_id = e.course_id
    group by c.course_id;
END $$
DELIMITER ;




