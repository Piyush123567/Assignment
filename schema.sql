DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS teams;
DROP TABLE IF EXISTS projects;
DROP TABLE IF EXISTS tasks;

CREATE TABLE users (
    user_id TEXT,
    name TEXT,
    role TEXT
);

CREATE TABLE teams (
    team_id TEXT,
    name TEXT
);

CREATE TABLE projects (
    project_id TEXT,
    team_id TEXT,
    name TEXT
);

CREATE TABLE tasks (
    task_id TEXT,
    project_id TEXT,
    assignee_id TEXT,
    name TEXT,
    completed INTEGER,
    due_date TEXT,
    created_at TEXT
);
