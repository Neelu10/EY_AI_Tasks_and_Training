Create Database CompanyDB;
Use CompanyDB;

Create table Departments(
dept_id int auto_increment primary key,
dept_name varchar(50) not null
);

Create table Employees(
emp_id int auto_increment primary key,
name varchar(50),
age int,
salary decimal(10,2),
dept_id int,
foreign key (dept_id) references Departments(dept_id)
);
Insert into Departments(dept_name) Values
('IT'),('HR'),('Finance'),('Sales');

INSERT INTO Employees (name, age, salary, dept_id) VALUES

('Rahul', 28, 55000, 1),   -- IT

('Priya', 32, 60000, 2),   -- HR

('Arjun', 25, 48000, 3),   -- Finance

('Neha', 30, 70000, 1),    -- IT

('Vikram', 35, 65000, 4);  -- Sales
ALTER TABLE Employees DROP FOREIGN KEY employees_ibfk_1;

 
TRUNCATE TABLE Employees;
TRUNCATE TABLE Departments;

INSERT INTO Departments (dept_name) VALUES
('IT'),         -- id = 1

('HR'),         -- id = 2

('Finance'),    -- id = 3

('Sales'),      -- id = 4

('Marketing');  -- id = 5  
INSERT INTO Employees (name, age, salary, dept_id) VALUE
('Rahul', 28, 55000, 1),   -- IT
('Priya', 32, 60000, 2),   -- HR
('Arjun', 25, 48000, NULL),-- 
('Neha', 30, 70000, 1),    -- IT
('Vikram', 35, 65000, 4);  -- Sales
 
Select e.name,e.salary, d.dept_name
from Employees e
Inner join Departments d
on e.dept_id=d.dept_id;

Select e.name,e.salary, d.dept_name
from Employees e
Right join Departments d
on e.dept_id=d.dept_id;

Select e.name,e.salary, d.dept_name
from Employees e
left join Departments d
on e.dept_id=d.dept_id

UNION

Select e.name,e.salary, d.dept_name
from Employees e
Right join Departments d
on e.dept_id=d.dept_id;  -- full join 

