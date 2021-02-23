### 512-游戏玩法分析ii

表Activity，字段：player_id, device_id，event_date，games_played 

其中(player_id, event_date) 是这个表的两个主键

查询每一个玩家首次登陆的设备名称



key：

- 题目信息给出主键，需要使用主键提升查询效率





#### 易错点：

直接在子查询中选，会出现不对应的情况，需要添加where

```sql
select player_id,device_id
from
(select player_id,device_id,min(event_date) first_login
from Activity 
group by player_id
order by player_id asc)
```



改正后：

```sql
select a.player_id,a.device_id
from Activity a,
(select player_id,device_id,min(event_date) first_login
from Activity 
group by player_id
order by player_id asc) b
where a.player_id=b.player_id and a.event_date=b.first_login
```



法一：

```sql
select player_id,device_id
from Activity
where (player_id,event_date) in
(select player_id,min(event_date)
from Activity 
group by player_id
order by player_id)
```



法二：窗口函数

```sql
select player_id,device_id
from
(select player_id,device_id,
row_number() over(partition by player_id order by event_date) rk
from Activity) a
where a.rk=1
```





### 534-iii

要求：查询 当前日期之前玩家所玩的游戏总数 



法一：

```sql
-- 窗口函数
select player_id,event_date,
sum(games_played) over(partition by player_id order by event_date) games_played_so_far
from Activity


-- 自连接，按条件过滤分组
select a1.player_id,a1.event_date,sum(a2.games_played) games_played_so_far
from Activity a1,Activity a2
where a1.player_id=a2.player_id -- 自连接
and a1.event_date>=a2.event_date -- 找到 时间在自己前面的数据，b表就是时间较小的
group by a1.player_id,a1.event_date
order by player_id,event_date
```



### 550-IV

要求：报告在首次登录的第二天再次登录的玩家的比率



法一：内连接 + 子查询 

```sql
select
round(count(distinct a.player_id)
    /(select count(distinct player_id) from Activity),2) fraction
from Activity a join Activity b on a.player_id=b.player_id 
where datediff(b.event_date,a.event_date)=1  -- 过滤出有第二天登陆的
and (a.player_id,a.event_date) in -- 挑出最小日期
(select player_id,min(event_date)
from Activity
group by player_id)


-- 使用小技巧优化，判断 min(date)+1 是否存在
select
round(count(distinct player_id)
      /(select count(distinct player_id) from Activity),2) fraction
from Activity
where (player_id,event_date) in
(select player_id,date(min(event_date)+1)
from Activity
group by player_id)
```



法二：**avg函数的使用**

用左表作为分母的筛选，右表当做分子的筛选，通过联结实现多重筛选

```sql
select 
-- is not null判断后，有event_date值的返回1，null的返回0，avg相当于求和后(即符合条件的id个数)除以总id数即所求比例
round(avg(t2.event_date is not null),2) fraction
from
(select player_id,min(event_date) first_login
from Activity
group by player_id) t1 -- t1是 首日登陆表
left join Activity t2 on t1.player_id=t2.player_id
and datediff(t2.event_date,t1.first_login)=1
```



法三：case when

```sql
select 
round(sum(case when datediff(event_date,first_login)=1 then 1 else 0 end)
      /(select count(distinct player_id) from Activity),2) fraction
from Activity t1,
(select player_id,min(event_date) first_login
from Activity
group by player_id) t2
where t1.player_id=t2.player_id
```



### 1097-V

需求：查询每个安装日期、当天安装游戏的玩家数量和第一天的留存时间

```
install_dt | installs | Day1_retention
```



法一：窗口函数

- **通用性强，可用来求3，7，30天的留存率**

- min() over() 求每个player_id 的首次安装日期，**再按注册日期分组，求与首次差为1的数量** 

```sql
-- 按首次安装日期分组，组里的player_id 就是安装游戏的玩家数量
SELECT
first_install AS install_dt,
COUNT(DISTINCT player_id) AS installs,
ROUND((SUM(IF(DATEDIFF(event_date,first_install)=1,1,0))) -- 统计日期与首次安装 差为1的总数
    /(COUNT(DISTINCT player_id)),2) AS Day1_retention 
FROM
(SELECT
player_id,event_date,MIN(event_date) over(partition by player_id) first_install
FROM Activity) t1
GROUP BY first_install
```



法二：

子查询+连接，较为繁琐

```sql
SELECT
t1.first_install install_dt,
COUNT(t1.player_id) installs,
ROUND(COUNT(t2.player_id)/COUNT(t1.player_id),2) Day1_retention
FROM
(SELECT
player_id,MIN(event_date) first_install
from Activity GROUP BY player_id) t1  -- 表1：首日安装日期
LEFT JOIN Activity t2 ON t1.player_id=t2.player_id
AND DATEDIFF(t2.event_date,t1.first_install)=1  -- 挑选出日期差为1的
GROUP BY t1.first_install
```

