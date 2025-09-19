SELECT e.name as Employee  FROM Employee  e 
JOIN Employee  m ON e.managerId = m.id where e.salary > m.salary