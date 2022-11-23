-- get last in of every user of a particular date
WITH today_attendance AS (
		SELECT * FROM attendance WHERE DATE(attendance.in_time) = %s
	),
	partition_attendance AS (
		SELECT *, ROW_NUMBER() OVER (PARTITION BY participant_id ORDER BY in_time DESC) AS row_num
		FROM today_attendance
	),
	last_in AS (
		SELECT *, DATE(in_time) FROM partition_attendance WHERE row_num = 1
	)
SELECT * FROM last_in;