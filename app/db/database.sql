-- CreateTable
CREATE TABLE IF NOT EXISTS attendance (
    id SERIAL NOT NULL,
    name TEXT NOT NULL,
    slack_id TEXT NOT NULL,
    in_time TIMESTAMP(3) NOT NULL,
    out_time TIMESTAMP(3),
    worked_time INTERVAL,
    on_break BOOLEAN NOT NULL DEFAULT false,

    CONSTRAINT attendance_pkey PRIMARY KEY (id)
);

-- CreateTable
CREATE TABLE IF NOT EXISTS break (
    id SERIAL NOT NULL,
    attendance_id INTEGER NOT NULL REFERENCES attendance(id),
    break_length INTERVAL NOT NULL,
    started TIMESTAMP(3) NOT NULL,
    ended TIMESTAMP(3),
    extra_time INTERVAL,

    CONSTRAINT break_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS participant (
    id SERIAL NOT NULL,
    slack_id TEXT NOT NULL,
    team_id  TEXT NOT NULL,
    name TEXT NOT NULL,
    tz TEXT
);

ALTER TABLE participant ADD CONSTRAINT slack_id_unique UNIQUE(slack_id);

CREATE TABLE IF NOT EXISTS team_break (
    id SERIAL NOT NULL,
    reason TEXT NOT NULL,
    started TIMESTAMP(3) NOT NULL,
    ended TIMESTAMP(3),

    CONSTRAINT team_break_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS project (
    id SERIAL NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
	completed BOOLEAN,

	CONSTRAINT project_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS task (
    id SERIAL NOT NULL,
    attendance_id INTEGER NOT NULL REFERENCES attendance(id),
    title TEXT NOT NULL,
    project TEXT,
    description TEXT,
	excuse TEXT,
	completed BOOLEAN,

	CONSTRAINT task_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS blocker (
    id SERIAL NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
	completed BOOLEAN,

	CONSTRAINT project_pkey PRIMARY KEY (id)
);

