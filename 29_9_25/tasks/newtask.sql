create database retailDB;
use retailDB;

Create table Customers(
customer_id int auto_increment primary key,
name varchar(50),
city varchar(40),
phone varchar(15));

Create table Products(
product_id int auto_increment primary key,
product_name varchar(50),
category varchar(40),
price decimal(10,2)
);

Create table Orders(
order_id int auto_increment primary key,
customer_id int,
order_date Date,
foreign key(customer_id) references Customers(customer_id));
 
Create table OrderDetails (
order_detail_id int auto_increment primary key,
order_id int,
product_id int,
qunatity int,
foreign key(order_id) references Orders(order_id),
foreign key(product_id)references Products(product_id));


INSERT INTO Customers (name, city, phone) VALUES
('Rahul', 'Mumbai', '9876543210'),
('Priya', 'Delhi', '9876501234'),
('Arjun', 'Bengaluru', '9876512345'),
('Neha', 'Hyderabad', '9876523456');


INSERT INTO Products (product_name, category, price) VALUES
('Laptop', 'Electronics', 60000.00),
('Smartphone', 'Electronics', 30000.00),
('Headphones', 'Accessories', 2000.00),
('Shoes', 'Fashion', 3500.00),
('T-Shirt', 'Fashion', 1200.00);


INSERT INTO Orders (customer_id, order_date) VALUES
(1, '2025-09-01'),
(2, '2025-09-02'),
(3, '2025-09-03'),
(1, '2025-09-04');


INSERT INTO OrderDetails (order_id, product_id, Qunatity) VALUES
(1, 1, 1),   -- Rahul bought 1 Laptop
(1, 3, 2),   -- Rahul bought 2 Headphones
(2, 2, 1),   -- Priya bought 1 Smartphone
(3, 4, 1),   -- Arjun bought 1 Shoes
(4, 5, 3);   -- Rahul bought 3 T-Shirts


DELIMITER $$
CREATE PROCEDURE GetAllProducts()
BEGIN
     SELECT product_id,product_name,category,price
     FROM products;
END$$
DELIMITER ;

CALL GetAllProducts();

DELIMITER $$

Create procedure GetOrdersWithCustomers()
Begin 
     select o.order_id,o.order_date , c.name as customer_name
     from Orders o
     join Customers c
     on o.customer_id=c.customer_id;
End$$
DELIMITER ;

Call GetOrdersWithCustomers();


DELIMITER $$
create procedure GetFullOrderDetails()
begin
select o.order_id,c.name as customer_name,p.product_name,od.qunatity,p.price,(od.qunatity*p.price) as total
from Orders o
JOIN Customers c ON o.customer_id=c.customer_id
JOIN OrderDetails od ON o.order_id=od.order_id
JOIN Products p ON od.product_id=p.product_id;
END$$

DELIMITER ;

Call GetFullOrderDetails();

DELIMITER $$
Create procedure GetCustomerOrders(IN cust_id INT)
Begin 
      select o.order_id,o.order_date,p.product_name,od.qunatity,p.price,(od.qunatity * p.price) as total
      from orders o
      join OrderDetails od on o.order_id=od.order_id
      join Products p on od.product_id=p.product_id
      where o.customer_id=cust_id;
End $$
DELIMITER $$;
call GetCustomerorders(1);


DELIMITER $$
Create procedure GetMonthlySales(in month_no int, in year_no int)

begin 
	select month(o.order_date) as month,year(o.order_date) as year,
    sum(od.qunatity *p.price) as total_sales
    from orders o 
    join OrderDetails od on o.order_id=od.order_id
    join products p on od.product_id=p.product_id
    where month(o.order_date)=month_no and year(o.order_date) = year_no
    group by month,year;
end $$
 
delimiter ;
call GetMonthlySales(9,2025);


DELIMITER $$
CREATE PROCEDURE GetTopProducts1()
BEGIN
SELECT p.product_name,
SUM(od.qunatity) AS total_sold,
SUM(od.qunatity * p.price) AS revenue
FROM  OrderDetails od
join Products p on od.product_id = p.product_id
GROUP BY p.product_id,p.product_name
order by revenue DESC
LIMIT 3;
END $$
DELIMITER ;
 
CALL GetTopProducts1();