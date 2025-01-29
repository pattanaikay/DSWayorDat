/*

Find the second highest salary of all departments in an office

*/

-- without using dense rank

SELECT department,
MAX(salary) AS second_highest_salary
FROM employees
WHERE 
salary NOT IN (SELECT MAX(salary) FROM employees GROUP BY departments)
GROUP BY department;

-- with using dense rank

SELECT salary, emp_id
FROM 
(
    SELECT salary, emp_id
    DENSE_RANK() OVER (ORDER BY salary DESC) AS rank
    FROM employees
) ranked_employees
WHERE
    rank = 2;

-- with using rank

SELECT salary, emp_id
FROM
(
    SELECT salary, emp_id
    RANK() OVER (ORDER BY salary DESC) AS rank
    FROM employees
) ranked_employees
WHERE
    rank = 2;


SELECT salary 
FROM employees
WHERE salary < (SELECT MAX(salary) FROM employees);