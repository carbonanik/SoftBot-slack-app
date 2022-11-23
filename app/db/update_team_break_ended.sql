
UPDATE team_break SET ended = NOW() WHERE id = (
	SELECT id FROM team_break ORDER BY started DESC LIMIT 1
) RETURNING *;