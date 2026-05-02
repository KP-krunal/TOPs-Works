create database tops_assignment;
use tops_assignment;

create table company(
companyID int primary key,
companyName varchar(45),
street varchar(45),
city varchar(45),
state varchar(2),
zip varchar(10)
);

-- 1) Statement to create the Contact table
create table contact(
contactId int primary key,
companyID int,
firstname varchar(45),
lastname varchar(45),
street varchar(45),
city varchar(45),
state varchar(2),
zip varchar(10),
Ismain boolean,
email varchar(45),
phone varchar(12),
foreign key (companyID) references company (companyID)
);

-- 2) Statement to create the Employee table
create table employee(
emplloyeeID int primary key,
firstname varchar(45),
lastname varchar(45),
salary decimal(10,2),
hiredate date,
jobtitle varchar(25),
email varchar(45),
phone varchar(12) 
);


-- 3) Statement to create the ContactEmployee table  
--    HINT: Use DATE as the datatype for ContactDate. It allows you to store the 
--    date in this format: YYYY-MM-DD (i.e., ‘2014-03-12’ for March 12, 2014).
create table contactEmployee(
contactemployeeID int primary key,
contactID int,
emplloyeeID int,
contactdate date,
descri varchar(100),
foreign key (contactID) references contact (contactID),
foreign key (emplloyeeID) references employee (emplloyeeID)
)