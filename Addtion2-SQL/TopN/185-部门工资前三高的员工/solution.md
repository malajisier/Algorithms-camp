### 法一：join和子查询

（1）前三高意味着 **不过超3个工资比这些值大**，统计了有多少人的工资比 e1.Salary 高

- 通俗理解：
  - 同一部门内 ，第一高工资 比他高的工资 个数为0 ,第二高工资 ,比他的高的 工资个数为1，第三高为2
  - 因此 只要查出 在同一部门内 其他的工资>该员工的薪资 的个数小于3 那么他就为同一部门的前三高工资 ，即为子查询里面的条件

```sql
select e1.Name Employee,e1.Salary
from Employee e1
where 3>
(select count(distinct e2.Salary)
from Employee e2
where e2.Salary>e1.Salary)
```



（2）join连接 来获得部门信息

```sql
select 
d.Name Department,e1.Name Employee,e1.Salary
from Employee e1
join Department d on e1.DepartmentId=d.Id
where 3>
(select count(distinct e2.Salary)
from Employee e2
where e2.Salary>e1.Salary
and e1.DepartmentId=e2.DepartmentId)
```







### 法二：窗口函数

```sql
select
Name Department,Employee,Salary
from
(select
d.Name,e.Name Employee,e.Salary,
dense_rank() over(partition by DepartmentId order by Salary desc) drk
from Employee e join Department d
on e.DepartmentId=d.Id) t1
where t1.drk<=3
```

