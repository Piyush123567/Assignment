# Assignment

# Asana Simulation Dataset

This project generates a synthetic Asana-like workspace dataset using Python and SQLite.

The dataset is created to simulate a large company’s project management data and can be used for research, evaluation, and testing of AI agents.

## Project Files

- `schema.sql` – Defines database tables
- `src/main.py` – Python script to generate data
- `asana_simulation.sqlite` – Generated SQLite database
- `requirements.txt` – Python dependencies

## Dataset Details

The generated database contains:
- 7,500 users
- 300 teams
- 2,000 projects
- 50,000 tasks

Task data includes realistic behavior such as:
- Unassigned tasks
- Completed and incomplete tasks
- Tasks with due dates and overdue tasks

## How to Run

1. Install dependencies:
```bash
pip install -r requirements.txt
