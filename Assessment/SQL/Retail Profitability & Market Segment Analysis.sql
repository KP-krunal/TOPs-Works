-- Assesment Mini Project
-- Title: Retail Profitability & Market Segment Analysis 
ALTER TABLE superstore
CHANGE `Row ID` row_id INT,
CHANGE `Order ID` order_id VARCHAR(50),
CHANGE `Order Date` order_date TEXT,
CHANGE `Ship Date` ship_date TEXT,
CHANGE `Ship Mode` ship_mode VARCHAR(50),
CHANGE `Customer ID` customer_id VARCHAR(50),
CHANGE `Customer Name` customer_name VARCHAR(100),
CHANGE `Product ID` product_id VARCHAR(50),
CHANGE `Sub-Category` sub_category VARCHAR(50),
CHANGE `Product Name` product_name VARCHAR(255);


-- Task 1
-- CREATE DATABASE assesment_pract;
USE assesment_pract;
DESC superstore;

-- Task 2
-- Check Discount Impact on Profit
SELECT 
	category,
    AVG(discount) AS Avg_Discount,
    AVG(profit) AS Avg_Profit
FROM superstore
GROUP BY category;

-- Find Loss Making Categories
SELECT 
	category,
    SUM(profit) AS Total_Profit
FROM superstore
GROUP BY category
HAVING SUM(profit) < 100;

-- Multi-Condition Filtering Query
SELECT * FROM superstore
	WHERE discount > 0.30
    AND profit < 0
    LIMIT 10 ;

-- Task 3
-- Identify underperforming product categories and regions 
-- by analyzing the relationship between discount rates and net profit margins.

-- Find Total Sales & Profit
SELECT 
	SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit
FROM superstore;

-- Region Wise Performance Report
SELECT 
	region,
	SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit
FROM superstore
GROUP BY region
ORDER BY Total_Profit DESC;

-- Category Wise Performance
SELECT 
	category,
	SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit
FROM superstore
GROUP BY category;


-- Summary of Loss-Making Transactions
SELECT
	Order_ID , Product_Name, category, region, 
    sales, discount, profit
    FROM superstore
    WHERE profit < 0
    ORDER BY profit
    LIMIT 30;