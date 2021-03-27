-- 法一：
select Name
from
(select CandidateId as id
from Vote
group by CandidateId
order by count(id) desc
limit 1) t1
join Candidate
on t1.id=Candidate.id

select Name 
from Candidate c left join Vote v
on c.id=v.CandidateId
group by v.CandidateId
order by count(CandidateId) desc
limit 1