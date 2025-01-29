/* 

Find the top 3 customers with the highest total order value.

*/

SELECT customer_id, sum(order_amount) as total_order_value
FROM orders
GROUP BY customer_id
ORDER BY total_order_value DESC
LIMIT 3;