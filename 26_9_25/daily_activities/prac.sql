INSERT INTO students( name,age,course,marks)
VALUES('Rahul',21,'ML',55);

INSERT INTO students( name,age,course,marks)
VALUES('Priya',22,'AI',88),('John',21,'AI',7);

select * from students;

select name,age,marks from students;
select * from students where marks > 80;

UPDATE students
set marks=95 , course='Advanced AI' where id=3;
-- update students SET course='AI'
delete from students where id =1;