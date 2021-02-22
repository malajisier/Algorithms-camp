### 法一：join和in语句

（1）首先 查每个部门的最高工资

```
select DepartmentId,max(Salary)
from Employee
group by DepartmentId
```

（2）再用 in连接表

```
select d.Name Department,e.Name Employee,Salary
from Employee e
join Department d on e.DepartmentId=d.Id
where 
(e.DepartmentId,Salary)
(select DepartmentId,max(Salary)
from Employee
group by DepartmentId)
```







### 法二：窗口函数

```sql
select
t1.Name Department,t1.Employee,t1.Salary
from
(select
d.Name,e.Name as Employee,e.Salary,
rank() over(partition by e.DepartmentId order by e.Salary desc) rk
from Employee e
join Department d
on e.DepartmentId=d.Id) t1
where t1.rk=1
```

