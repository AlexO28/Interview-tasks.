select unique(t1.repository.name) from publicdata:samples.github_nested as t1 join
(select repository.name, count(unique(repository.url)) as cnt 
from publicdata:samples.github_nested
group by repository.name 
order by cnt desc limit 1) as t2
on t1.repository.name = t2.repository.name

select tt2.repository.url as repository.url, avg(-tt2.myval+tt2.nt) as avgtimediff from 
(select tt.repository.url as repository.url, tt.nt as nt, lag(tt.nt, 1)
over (partition by tt.repository.url
order by tt.nt
) myval,
 from
(select repository.url, timestamp_to_sec(timestamp(regexp_replace(substr(repository.pushed_at, 1, 20), '/', '-')
 + substr(repository.pushed_at, -5, 3) + ':' + substr(repository.pushed_at, -2, 2))) as nt
from publicdata:samples.github_nested) as tt
) as tt2
group by repository.url
order by repository.url

select tt2.repository.url as tt2, tt2.nt as repository.pushed_at,
tt.size-myval as sizechange from
(select tt.repository.url as repository.url, tt.nt as nt, tt.size, lag(tt.size, 1)
over (partition by tt.repository.url
order by tt.nt
) myval,
 from
(select repository.url, avg(repository.size) as size, timestamp(regexp_replace(substr(repository.pushed_at, 1, 20), '/', '-')
 + substr(repository.pushed_at, -5, 3) + ':' + substr(repository.pushed_at, -2, 2)) as nt
from publicdata:samples.github_nested
group by repository.url, nt
) as tt) as tt2
order by tt2.repository.url, tt2.nt
