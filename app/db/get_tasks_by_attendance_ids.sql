SELECT task.* FROM attendance
INNER JOIN "_attendanceTotask"
  ON attendance.id = "_attendanceTotask"."A"
INNER JOIN task
  ON "_attendanceTotask"."B" = task.id
WHERE attendance.id IN %s;
