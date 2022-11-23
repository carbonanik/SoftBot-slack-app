select * from attendance where id=(
	select id from attendance
	where slack_id = %s
	order by in_time desc limit 1
) and out_time is null;