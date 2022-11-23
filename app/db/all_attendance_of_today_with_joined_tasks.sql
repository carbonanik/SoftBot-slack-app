SELECT
attendance.id AS attendance_id,
attendance.in_time AS attendance_in_time,
attendance.out_time AS attendance_out_time,
task.id AS task_id,
task.started_at AS task_started_at,
task.ended_at AS task_ended_at,
task.status AS task_status

FROM attendance
INNER JOIN "_attendanceTotask"
  ON attendance.id = "_attendanceTotask"."A"
INNER JOIN task
  ON "_attendanceTotask"."B" = task.id
WHERE DATE(in_time) = DATE(NOW())