/*

Write a SQL query to find the top 5 customers by total purchase amount

*/

SELECT CustomerName, SUM(OrderAmount) as TotalPurchaseAmount
FROM Customers
JOIN Orders on Customers.CustomerID = Orders.CustomerID
GROUP BY CustomerName 
ORDER BY TotalPurchaseAmount DESC
LIMIT 5