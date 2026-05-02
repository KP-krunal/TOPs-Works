use tops_assignment;

INSERT INTO company VALUES
(1, 'TechNova', 'SG Highway', 'Ahmedabad', 'GJ', '380015'),
(2, 'InnoSoft', 'Ring Road', 'Surat', 'GJ', '395007'),
(3, 'DataCorp', 'MG Road', 'Mumbai', 'MH', '400001'),
(4, 'AlphaSys', 'Banjara Hills', 'Hyderabad', 'TS', '500034'),
(5, 'NextGen', 'Whitefield', 'Bangalore', 'KA', '560066'),
(6, 'SkyTech', 'Sector 62', 'Noida', 'UP', '201309'),
(7, 'BrightIT', 'Salt Lake', 'Kolkata', 'WB', '700091'),
(8, 'CloudNet', 'Anna Nagar', 'Chennai', 'TN', '600040'),
(9, 'FutureSoft', 'Civil Lines', 'Jaipur', 'RJ', '302006'),
(10, 'SmartSys', 'Sector 17', 'Chandigarh', 'CH', '160017');

INSERT INTO contact VALUES
(1, 1, 'Raj', 'Patel', 'Navrangpura', 'Ahmedabad', 'GJ', '380009', 1, 'raj@technova.com', '9876543210'),
(2, 2, 'Amit', 'Shah', 'Adajan', 'Surat', 'GJ', '395009', 1, 'amit@innosoft.com', '9876543211'),
(3, 3, 'Neha', 'Mehta', 'Andheri', 'Mumbai', 'MH', '400053', 1, 'neha@datacorp.com', '9876543212'),
(4, 4, 'Ravi', 'Kumar', 'Jubilee Hills', 'Hyderabad', 'TS', '500033', 1, 'ravi@alphasys.com', '9876543213'),
(5, 5, 'Priya', 'Rao', 'Marathahalli', 'Bangalore', 'KA', '560037', 1, 'priya@nextgen.com', '9876543214'),
(6, 6, 'Suresh', 'Yadav', 'Sector 18', 'Noida', 'UP', '201301', 1, 'suresh@skytech.com', '9876543215'),
(7, 7, 'Anjali', 'Das', 'Dum Dum', 'Kolkata', 'WB', '700028', 1, 'anjali@brightit.com', '9876543216'),
(8, 8, 'Karthik', 'Iyer', 'T Nagar', 'Chennai', 'TN', '600017', 1, 'karthik@cloudnet.com', '9876543217'),
(9, 9, 'Pooja', 'Singh', 'Malviya Nagar', 'Jaipur', 'RJ', '302017', 1, 'pooja@futuresoft.com', '9876543218'),
(10, 10, 'Manoj', 'Verma', 'Sector 22', 'Chandigarh', 'CH', '160022', 1, 'manoj@smartsys.com', '9876543219');


INSERT INTO employee VALUES
(1, 'Arjun', 'Patel', 50000.00, '2022-01-15', 'Developer', 'arjun@gmail.com', '9000000001'),
(2, 'Kiran', 'Shah', 55000.00, '2021-03-20', 'Analyst', 'kiran@gmail.com', '9000000002'),
(3, 'Meera', 'Joshi', 60000.00, '2020-07-10', 'Manager', 'meera@gmail.com', '9000000003'),
(4, 'Rahul', 'Nair', 52000.00, '2023-02-18', 'Tester', 'rahul@gmail.com', '9000000004'),
(5, 'Sneha', 'Reddy', 58000.00, '2022-09-25', 'HR', 'sneha@gmail.com', '9000000005'),
(6, 'Vikas', 'Singh', 62000.00, '2019-11-11', 'Team Lead', 'vikas@gmail.com', '9000000006'),
(7, 'Divya', 'Gupta', 54000.00, '2021-06-30', 'Designer', 'divya@gmail.com', '9000000007'),
(8, 'Aakash', 'Verma', 57000.00, '2020-12-05', 'Support', 'aakash@gmail.com', '9000000008'),
(9, 'Rohit', 'Sharma', 65000.00, '2018-08-22', 'Architect', 'rohit@gmail.com', '9000000009'),
(10, 'Nikita', 'Kapoor', 53000.00, '2023-05-01', 'Intern', 'nikita@gmail.com', '9000000010');


INSERT INTO contactEmployee VALUES
(1, 1, 1, '2024-01-01', 'Project discussion'),
(2, 2, 2, '2024-01-05', 'Requirement gathering'),
(3, 3, 3, '2024-01-10', 'Client meeting'),
(4, 4, 4, '2024-01-15', 'Testing update'),
(5, 5, 5, '2024-01-20', 'HR discussion'),
(6, 6, 6, '2024-01-25', 'Team meeting'),
(7, 7, 7, '2024-02-01', 'Design review'),
(8, 8, 8, '2024-02-05', 'Support call'),
(9, 9, 9, '2024-02-10', 'Architecture planning'),
(10, 10, 10, '2024-02-15', 'Intern training');
