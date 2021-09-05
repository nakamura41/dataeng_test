SELECT 
  cu.Name AS Name, SUM(cr.Price) AS TotalSpending
FROM
dealership.Customer cu
INNER JOIN
dealership.Sale s
ON cu.Id = s.CustomerId
INNER JOIN
dealership.Car cr
ON cr.Id = s.CarId
GROUP BY
cu.Name