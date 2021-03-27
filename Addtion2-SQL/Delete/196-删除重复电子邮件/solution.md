1. delete+where

```sql
delete p1  -- 如果使用了表别名，delete后必须要加别名
from Person p1,Person p2
where
p1.Email=p2.Email and p1.Id>p2.Id
```



2. min + in字句

```sql
delete from Person
where Id not in -- 删除 除minid之外的id
(select minid
from
(select
min(Id) over(partition by Email) minid
from Person) t1)
```

