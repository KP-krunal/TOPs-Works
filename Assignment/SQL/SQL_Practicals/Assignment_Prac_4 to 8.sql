use tops_assignment;
desc employee;

-- 4) In the Employee table, the statement that changes Lesley Bland’s phone number 
--    to 215-555-8800  
select * from employee;
update employee
set phone = 9000000110
where emplloyeeID = 1;

-- 5) In the Company table, the statement that changes the name of “Urban 
--    Outfitters, Inc.” to “Urban Outfitters”. 
select * from company;
update Company set CompanyName = 'TechNova Pvt. Ltd.' where CompanyName = 'TechNova Ltd.';


-- 6)  In ContactEmployee table, the statement that removes Dianne Connor’s contact 
--     event with Jack Lee (one statement). 
select * from contactemployee;
select * from contact;
delete from contactemployee
where contactemployeeID = 10;


-- 7) Write the SQL SELECT query that displays the names of the employees that 
--    have contacted Toll Brothers (one statement). Run the SQL SELECT query in 
--    MySQL Workbench. Copy the results below as well.
select * from company;
select * from employee;
desc contactemployee;
desc contact;

SELECT employee.firstname, employee.lastname
FROM employee
JOIN contactemployee ON employee.emplloyeeID = contactemployee.emplloyeeID
JOIN contact ON contactemployee.contactID = contact.contactID
JOIN company ON contact.companyID = company.companyID
WHERE company.companyName = 'NextGen';


-- 8) What is the significance of “%” and “_” operators in the LIKE statement?
select * from employee where firstname like 'A%'; -- use of the '%' Symbol
select * from employee where firstname like 'A_' -- use of the '_' Symbol

