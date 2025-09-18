-- Write your PostgreSQL query statement below


SELECT COALESCE ((SELECT DISTINCT salary as SecondHighestSalary FROM Employee ORDER BY salary  DESC OFFSET 1 LIMIT 1),null) as secondhighestsalary 