-- 法一：order by 中也可使用聚合函数
-- 统计每个问题的出现次数 和 回答次数

select
question_id as survey_log
from survey_log
group by question_id
order by sum(if(action='answer',1,0)) / sum(if(action='show',1,0)) desc
limit 1