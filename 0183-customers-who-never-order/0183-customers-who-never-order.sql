Select c.name As  Customers 
from Customers c
left join Orders o
on c.id=O.customerId
where o.customerID IS NULL;
