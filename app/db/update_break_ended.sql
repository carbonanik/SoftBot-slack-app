-- break the break / update break ended
--
-- need 1 value - slack_id
DO $$ DECLARE
    out_time_v TIMESTAMP;
    id_v INT;
	on_break_v BOOLEAN;
	
	break_id_v INT;
	break_ended_v TIMESTAMP;
BEGIN
    SELECT id, out_time, on_break INTO id_v, out_time_v, on_break_v FROM attendance
    WHERE slack_id = %s
    ORDER BY in_time DESC limit 1;
	
	SELECT id, ended INTO break_id_v, break_ended_v FROM break 
	WHERE attendance_id=id_v 
	ORDER BY started DESC LIMIT 1;

    IF id_v IS NOT NULL AND out_time_v IS NULL AND on_break_v THEN
        UPDATE attendance SET on_break = FALSE WHERE id=id_v; 
		
		IF break_ended_v IS NULL AND break_id_v IS NOT NULL THEN
			UPDATE break SET ended=NOW(), extra_time=
			CASE
				WHEN NOW()>started+break_length THEN NOW()-started+break_length
				ELSE NULL
			END
			WHERE id = break_id_v;	
		END IF;
		
		RAISE NOTICE 'Successfully updated';
	ELSE
		RAISE NOTICE 'Can not update';
    END IF;

END $$;

