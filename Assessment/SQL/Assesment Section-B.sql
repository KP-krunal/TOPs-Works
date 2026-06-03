-- Assesment Practicals

-- CREATE DATABASE assesment_pract;
SHOW TABLES FROM assesment_pract;
USE assesment_pract;
DESC superstore;

SELECT * FROM superstore;

-- 1. Execute a query to retrieve the first 20 records from the orders table to verify data ingestion. 
SELECT * FROM superstore LIMIT 20;

-- 2. Select Order ID, Order Date, Sales, and Profit, applying a column alias to 
--    display Sales as Total_Sales
SELECT 'Order ID', 'Order Date', Sales AS Total_Sales, Profit
FROM superstore;

-- 3. Filter the dataset to isolate all high-value transactions where the Sales figure 
--    exceeds 5000.
SELECT * FROM superstore
WHERE Sales > 5000;

-- 4. Generate a report of the top 10 most profitable orders by sorting the records 
--    by Profit in descending order
SELECT * FROM superstore
ORDER BY Profit DESC
LIMIT 10;