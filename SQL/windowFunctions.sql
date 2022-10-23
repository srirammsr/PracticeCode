use mydb
select  * from Superstore
select Order_ID,Order_Date,Ship_Mode,Customer_Name,Sales  from superstore order by Ship_Mode
select sub_category,sum(sales) as TotalSales 
	from Superstore 
	group by 
		Sub_Category

--ship_mode wise total sales. The following SQL query yields correct results
select  Ship_Mode,sum(Sales) over (partition by ship_mode) as 'TotalSales '    from superstore
--OR
select Order_ID, Ship_Mode,sales,sum(Sales) over (partition by ship_mode order by ship_mode rows between unbounded preceding and unbounded following ) as K from superstore

--ship_mode wise total sales. The following SQL query considers only the previous N number of rows for calculating sum of sales. 
--It looks like cumulative summation of salaries. Only previous rows sales is considered.
select Order_ID, Ship_Mode,sales,sum(Sales) over (order by sales) as Total,
								avg(Sales) over (order by sales) aS Average,
								Count(Sales) over (order by sales) as Count from superstore



select * from sales.order_items

--Order Id wise sum of sales and average of sales

select sales.order_items.order_id,sum(sales.order_items.list_price*sales.order_items.quantity) over(partition by order_id order by order_id) as Total,
	avg(sales.order_items.list_price*sales.order_items.quantity) over(partition by order_id order by order_id) as average from sales.order_items


--lets find top 3 sales against each ship mode
--First extract all records with rank values:
select ship_mode,customer_name,sales,rank() over(partition by ship_mode order by sales desc) as  rnk from superstore
select ship_mode,customer_name,sales,row_number() over(partition by ship_mode order by sales desc) as  rnk from superstore
select ship_mode, count(ship_mode) from Superstore group by Ship_Mode

select * from (
	select ship_mode,customer_name,sales,rank() over(partition by ship_mode order by sales desc) as  rnk from superstore) k 
	where k.rnk <4

	SELECT DISTINCT TOP 5 sales  
      FROM Superstore  
      ORDER BY sales DESC 

select top 1 sales from(
	select top 2 sales from Superstore order by sales desc
	)A order by Sales


	select ROW_NUMBER() over(order by sales desc) as seq, Sales from Superstore

	SELECT 
  ROW_NUMBER() OVER(ORDER BY name ASC) AS Row#,
  name, recovery_model_desc
FROM sys.databases 
WHERE database_id < 5;

