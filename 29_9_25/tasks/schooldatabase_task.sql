create database SchoolDataBase;
use SchoolDataBase;

create table teachers(
teacher_id int auto_increment primary key,
name varchar(50),
subject_id int);

create table Subjects (
subject_id int auto_increment primary key,
subject_name varchar(50) );
INSERT INTO Subjects (subject_name) VALUES

('Mathematics'),   -- id = 1

('Science'),       -- id = 2

('English'),       -- id = 3

('History'),       -- id = 4

('Geography');     -- id = 5 (no teacher yet)

 INSERT INTO Teachers (name, subject_id) VALUES
('Rahul Sir', 1),   -- Mathematics
('Priya Madam', 2), -- Science
('Arjun Sir', NULL),-- No subject assigned
('Neha Madam', 3);  -- English


Select t.teacher_id,t.name,s.subject_name
from teachers t
inner join Subjects s
ON s.subject_id=t.subject_id;

Select t.teacher_id,t.name,s.subject_name
from teachers t
left join Subjects s
ON s.subject_id=t.subject_id;

Select t.teacher_id,t.name,s.subject_name
from teachers t
right join Subjects s
ON s.subject_id=t.subject_id;

Select t.teacher_id,t.name,s.subject_name
from teachers t
left join Subjects s
ON s.subject_id=t.subject_id

Union

Select t.teacher_id,t.name,s.subject_name
from teachers t
right join Subjects s
ON s.subject_id=t.subject_id;