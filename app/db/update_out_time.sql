-- update out_time in attendance where out_time is null
--
-- need 1 value - slack_id
--
-- update out time function
CREATE OR REPLACE FUNCTION update_out_time(slack_id_p TEXT)
RETURNS SETOF attendance AS $$
DECLARE
    out_time_v TIMESTAMP;
	in_time_v TIMESTAMP;
    id_v INT;
BEGIN
    SELECT id, in_time, out_time INTO id_v, in_time_v, out_time_v FROM attendance
    WHERE slack_id = slack_id_p
    ORDER BY in_time DESC LIMIT 1;

    IF id_v IS NOT NULL AND out_time_v IS NULL THEN
        UPDATE attendance SET out_time=NOW(), worked_time=NOW()-in_time_v, on_break=FALSE WHERE id=id_v;
		RETURN QUERY SELECT * FROM attendance WHERE id=id_v;
		RAISE NOTICE 'Inserted';
	ELSE
-- 		RETURN NULL;
		RAISE NOTICE 'Can not insert';
    END IF;
END $$ LANGUAGE plpgsql;
