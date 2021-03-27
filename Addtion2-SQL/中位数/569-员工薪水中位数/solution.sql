-- 法一：内连接
select Id,t1.Company,Salary
from
(select Id,Company,Salary,
row_number() over(partition by Company order by Salary) rk
from Employee) t1
inner join
(select Company,count(*) total 
from Employee
group by Company) t2
on t1.Company=t2.Company and rk between total/2 and total/2+1

-- 
select Id, Company, Salary
from 
(select  *,
        count(id) over (partition by Company) num,
        row_number() over (partition by Company order by salary) rn 
    from employee e1) t
where rn between num/2 and num/2+1