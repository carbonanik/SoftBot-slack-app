-- insert break if in attendance out_time is null and on_break is false
--
-- need 2 value - slack_id - break_length
-- FUNCTION
CREATE OR REPLACE FUNCTION inset_break_if_possible(slack_id_p TEXT, break_length_p INTERVAL)
RETURNS SETOF break AS $$
DECLARE
    out_time_v TIMESTAMP;
    id_v INT;
	on_break_v BOOLEAN;
BEGIN
    SELECT id, out_time, on_break INTO id_v, out_time_v, on_break_v FROM attendance
    WHERE slack_id = slack_id_p
    ORDER BY in_time DESC limit 1;

    IF id_v IS NOT NULL AND out_time_v IS NULL AND NOT on_break_v THEN
        UPDATE attendance SET on_break = TRUE WHERE id=id_v;
        RETURN QUERY INSERT INTO break (attendance_id, break_length, started) VALUES (id_v, break_length_p, NOW()) RETURNING *;
		RAISE NOTICE 'Successfully Inserted';
	ELSE
		RAISE NOTICE 'Can not insert';
    END IF;

END $$ LANGUAGE plpgsql;
