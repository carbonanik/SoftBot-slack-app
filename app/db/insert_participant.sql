INSERT INTO participant (created_at, updated_at, slack_id, name, email, phone, designation)
VALUES (NOW(), NOW(), %s, %s, %s, %s, %s) RETURNING *;
