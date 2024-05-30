select 
F.parcel_id, F.order_id, E.order_status, F.parcel_status,
case when E.dttm < F.dttm then E.dttm else F.dttm end as dttm
from
(select A.order_id, A.order_status, A.dttm, 
min(case when B.dttm is null then datetime('now') else B.dttm end) as next_dttm
from orders as A
left join orders as B
on (A.order_id = B.order_id) and (B.dttm > A.dttm)
group by A.order_id, A.order_status, A.dttm) as E
inner join
(select C.parcel_id, C.order_id, C.parcel_status, C.dttm,
min(case when D.dttm is null then datetime('now') else D.dttm end) as next_dttm
from parcel_status as C
left join parcel_status as D
on (C.parcel_id = D.parcel_id) and (C.order_id = D.order_id) and
(C.parcel_status = D.parcel_status) and (D.dttm > C.dttm)
group by C.parcel_id, C.order_id, C.parcel_status, C.dttm) as F
on (E.order_id = F.order_id) and 
(((F.dttm >= E.dttm) and (F.dttm <= E.next_dttm))
or ((E.dttm >= F.dttm) and (E.dttm <= F.next_dttm)))
order by order_id asc, parcel_id asc, dttm asc
