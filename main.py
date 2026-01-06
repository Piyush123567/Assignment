import sqlite3
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

# -----------------------
# CONNECT TO DATABASE
# -----------------------
conn = sqlite3.connect("asana_simulation.sqlite")
cursor = conn.cursor()

# -----------------------
# CREATE TABLES (VERY IMPORTANT)
# -----------------------
with open("schema.sql", "r") as f:
    cursor.executescript(f.read())

print("Tables created")

# -----------------------
# GENERATE USERS
# -----------------------
NUM_USERS = 7500
for i in range(NUM_USERS):
    cursor.execute(
        "INSERT INTO users VALUES (?, ?, ?)",
        (f"user_{i}", fake.name(), "Engineer")
    )
print("Users generated")

# -----------------------
# GENERATE TEAMS
# -----------------------
NUM_TEAMS = 300
for i in range(NUM_TEAMS):
    cursor.execute(
        "INSERT INTO teams VALUES (?, ?)",
        (f"team_{i}", f"Team_{i}")
    )
print("Teams generated")

# -----------------------
# GENERATE PROJECTS
# -----------------------
NUM_PROJECTS = 2000
for i in range(NUM_PROJECTS):
    cursor.execute(
        "INSERT INTO projects VALUES (?, ?, ?)",
        (f"project_{i}", f"team_{i % NUM_TEAMS}", fake.bs())
    )
print("Projects generated")

# -----------------------
# GENERATE TASKS (REALISTIC)
# -----------------------
NUM_TASKS = 50000
now = datetime.now()

for i in range(NUM_TASKS):
    task_id = f"task_{i}"
    project_id = f"project_{i % NUM_PROJECTS}"
    task_name = fake.sentence()

    # 15% unassigned
    assignee_id = None if random.random() < 0.15 else f"user_{random.randint(0, NUM_USERS - 1)}"

    # 70% completed
    completed = 1 if random.random() < 0.7 else 0

    created_at = now - timedelta(days=random.randint(1, 180))

    # 10% no due date
    if random.random() < 0.10:
        due_date = None
    else:
        due_date = created_at + timedelta(days=random.randint(3, 45))

    # overdue tasks
    if completed == 0 and random.random() < 0.10:
        due_date = now - timedelta(days=random.randint(1, 30))

    cursor.execute(
        "INSERT INTO tasks VALUES (?, ?, ?, ?, ?, ?, ?)",
        (
            task_id,
            project_id,
            assignee_id,
            task_name,
            completed,
            due_date.isoformat() if due_date else None,
            created_at.isoformat()
        )
    )

print("Tasks generated")

# -----------------------
# SAVE & CLOSE
# -----------------------
conn.commit()
conn.close()

print("Asana simulation database generated successfully")
# -----------------------
# QUICK VERIFICATION
# -----------------------
conn = sqlite3.connect("asana_simulation.sqlite")
cursor = conn.cursor()

tables = ["users", "teams", "projects", "tasks"]

for table in tables:
    cursor.execute(f"SELECT COUNT(*) FROM {table}")
    count = cursor.fetchone()[0]
    print(f"{table}: {count}")

conn.close()
