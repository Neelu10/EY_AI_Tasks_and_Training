Create database if not exists RetailNF;
use retailNF;

CREATE TABLE BadOrders(
   order_id INT PRIMARY KEY,
   order_date DATE,
   customer_id INT,
   customer_name VARCHAR(50),
   customer_city VARCHAR(50),
   product_id VARCHAR(200),
   product_name VARCHAR(200),
   unit_prices VARCHAR(200),
   quantities VARCHAR(200),
   order_total DECIMAL(10,2)
   );
 INSERT INTO BadOrders VALUES
-- order_id, date, cust, name, city,     pids,      pnames,                   prices,        qtys,    total
(101, '2025-09-01', 1, 'Rahul', 'Mumbai', '1,3',    'Laptop,Headphones',      '60000,2000',  '1,2',   64000.00),
(102, '2025-09-02', 2, 'Priya', 'Delhi',  '2',      'Smartphone',             '30000',       '1',     30000.00);


CREATE TABLE Orders1NF(
order_id INT Primary key,
order_date Date,
customer_id INT,
customer_name VARCHAR(50),
customer_city VARCHAR(50)
);

Create table OrderItems_1NF(
order_id INT,
line_no INT,
product_id INT,
product_name varchar(50),
unit_price varchar(50),
quantity INT,
primary key (order_id,line_no),
foreign key(order_id) references Orders1NF(order_id)
);  

Insert into Orders1NF
select order_id,order_date,customer_id,customer_name,customer_city
from BadOrders;

Insert into OrderItems_1NF values
(101,1,1,'laptop',60000,1),
(101,2,3,'headphones',2000,2);

Insert into OrderItems_1NF values
(102,1,2,'Smartphone',30000,1);

