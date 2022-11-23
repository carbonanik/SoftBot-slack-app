-- need 3 value - slack_id - name

-- insert attendance
-- if not already have a insert value where
-- in_time is in same day and
-- out_itme is null
CREATE OR REPLACE FUNCTION in_attendance_if_not_already(slack_id_p TEXT, name_p TEXT)
RETURNS SETOF attendance AS $$
DECLARE
    in_count_v INT;
BEGIN
    SELECT count(*) INTO in_count_v FROM attendance
	WHERE slack_id=slack_id_p AND in_time > NOW() - INTERVAL '1 day' AND out_time IS NULL;

    IF in_count_v = 0 THEN
        RETURN QUERY INSERT INTO attendance (name, slack_id, in_time) VALUES (name_p, slack_id_p, NOW()) RETURNING *;
        RAISE NOTICE 'Inserted successfully';
    ELSE
        RAISE EXCEPTION 'Can not insert';
    END IF;

END $$ LANGUAGE plpgsql;