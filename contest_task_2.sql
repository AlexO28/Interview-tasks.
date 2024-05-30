select C.order_id, C.item_id,
case when D.cost is null then 0 else round(C.item_count*(D.cost+0.0)/(B.total_count+0.0), 2) end as item_delivery_cost
from orders as C inner join
(select A.order_id, sum(A.item_count) as total_count from orders as A
group by A.order_id) as B
on C.order_id = B.order_id
left join delivery_costs as D
on C.order_id = D.order_id
