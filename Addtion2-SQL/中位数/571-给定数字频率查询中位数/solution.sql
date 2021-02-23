-- 法一：
-- 新增两列，将从后往前和从前往后的频数相加，两个数都需要大于等于总数一半，再取平均
select avg(number) as median
from
(select Number, frequency,
        sum(frequency) over(order by number asc) as total,
        sum(frequency) over(order by number desc) as total1
from Numbers
order by number asc)as a
where total>=(select sum(frequency) from Numbers)/2
and total1>=(select sum(frequency) from Numbers)/2

-- 另一张写法
select
round(avg(number), 1) median
from
(select number,
sum(Frequency) over(order by number) ascnum,
sum(Frequency) over(order by number desc) descnum
from Numbers) t1,
(select sum(Frequency) total
from Numbers) t2
where ascnum>=total/2 and descnum>=total/2