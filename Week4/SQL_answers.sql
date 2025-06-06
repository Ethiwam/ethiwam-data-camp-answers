-- Filename: SQL_answers.sql
-- Coder: Ethan Iwama
-- Purpose: Holds my answers to the SQL questions.

--Q1. Pull total number of orders that were completed on 18th March 2023
--    with the first name ‘John’ and last name Doe’
SELECT COUNT(*) FROM Sales S
JOIN Customers C ON S.Customer_id=C.Customer_id
WHERE C.First_name='John' AND C.Last_name='Doe' AND S.Date='2024-03-18';

--Q2. Pull total number of customers that purchased in January 2023 and
--    the average amount spend per customer
SELECT C.Customer_id, C.First_name, C.Last_name, AVG(REVENUE) FROM Customers C
JOIN Sales S ON S.Customer_id=C.Customer_id
WHERE Date BETWEEN '2023-01-01' AND '2023-01-31'
GROUP BY C.Customer_id;

--Q3. Pull the departments that generated less than $600 in 2022
SELECT I.Department, SUM(S.Revenue) AS Rev FROM Items I
JOIN Sales S ON S.Item_id=I.Item_id
WHERE S.Date BETWEEN '2022-01-01' AND '2022-12-31'
GROUP BY I.Department
HAVING Rev < 600;

--Q4. What is the most and least revenue we have generated by an order
SELECT MAX(Revenue), MIN(Revenue) FROM SALES;

--Q5. What were the orders that were purchased in our most lucrative order
SELECT * FROM Sales
WHERE Revenue=(SELECT MAX(Revenue) FROM Sales);