use schoolDB;
drop table if exists employees;
create table employees(
id INT auto_increment primary key,
name varchar(50) not null,
age int,
department varchar(50),
salary decimal(10,2));

INSERT INTO employees(name,age,department,salary)
VALUES('Jake',24,'Tax',600000.00);
INSERT INTO employees(name,age,department,salary)
VALUES('Jay',23,'Assurance',650000.00);


INSERT INTO employees(name,age,department,salary)
VALUES('Tisha',23,'Assurance',650000.00),('Kirsten',24,'Tax',600000.00);

select * from employees;

select name,age,salary from employees;
select * from employees where salary>600000.00;

update employees set department='Consulting' where id=2;
delete from employees where id=3;
