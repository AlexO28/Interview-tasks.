select A.dt, coalesce(count(acc_number), 0) as cnt, coalesce(sum(fin_amount), 0) as summa
from Dates as A
left join ACCOUNT as B
on (B.close_date is null and B.open_date <= A.dt) or
(B.close_date is not null and B.open_date <= A.dt and A.dt <= B.close_date)
group by A.dt
