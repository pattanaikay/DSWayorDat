/* 

Find the employees who earn more than the average salary of their department.

*/

SELECT e.employee_id, e.department, e.salary
FROM employees e
JOIN 
(
    SELECT department, AVG(salary) as avg_dept_salary
    FROM employees
    GROUP BY department
)
ON e.department = d.department
WHERE
e.salary > d.avg_dept_salary
