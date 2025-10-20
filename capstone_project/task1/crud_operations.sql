Create database retail;
Use Retail;

Create Table products(
product_id VARCHAR(10) primary key,
name VARCHAR(50),
category VARCHAR(30),
price decimal(10,2));

Create Table Customers1(
customer_id VARCHAR(10) primary key,
name VARCHAR(50),
email VARCHAR(100),
country VARCHAR(20));

Insert into products Values(
'P101','Laptop','Electronics',800),
('P102','Mouse','Accessories',20),
('P103','Keyboard','Accessories',35),
('P104','Headphones','Audio',50);

insert into Customers1 Values(
'C001','Neha','neha@example.com','India'),
('C002','Ali','ali@example.com','UAE'),
('C003','Sophia','sophia@example.com','UK');

Select * from products;
Select * from Customers1;

-- Task 1 Add a new product
insert into products value('P105','Tablet','Electronics','1000');


-- Task 2 update a product price
update products SET price = 750 where product_id='P101';

-- Task 3 delete a customer
delete from Customers1 where customer_id='C002';

-- Task 4 list all customers frm India
Select * from Customers1 where country='India';


