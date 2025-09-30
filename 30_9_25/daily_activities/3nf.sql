
create table City1(
	city_id int primary key,
    city_name varchar(50),
    state varchar(50)
);
 
create table Customer_3NF1(
	customer_id int primary key,
    customer_name varchar(50),
    city_id int,
    foreign key (city_id) references City1(city_id)
);
 
create Table Product_3NF1 like Products_2NF;
insert into Product_3NF1 Select * from Products_2NF;
 
create table Orders_3NF1 like Orders_2NF;
create table OrderItems_3NF1 like ORderItems_2NF;
 
insert into City1 Values
(10,"Mumbai","Maharashtra"),
(20,"Delhi","Delhi");
 
insert into Customer_3NF1 values
(1,"Rahul",10),
(2,"Priya",20);
 
insert into Orders_3NF select * from Orders_2NF;
insert into OrderItems_3NF select * from OrderItems_2NF;

select * from City1