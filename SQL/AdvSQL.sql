use myDB

-- Fetch 1 record per city from doctors table
select * from doctors --first see all the records

select *, row_number() over(partition by city order by city) X from doctors where X =1;



--From the doctors table, fetch the details of doctors who work in the same hospital but in different specialty
select * from doctors d1 join doctors d2 on d1.name <>d2.name and d1.hospital =d2.hospital and d1.speciality=d2.speciality

