from faker import Faker
import psycopg2
import random

fake = Faker()
conn = psycopg2.connect("dbname=university user=postgres password=password host=localhost")
cur = conn.cursor()

groups = ['Group A', 'Group B', 'Group C']
for group in groups:
    cur.execute("INSERT INTO groups (name) VALUES (%s)", (group,))

group_ids = range(1, len(groups) + 1)
for _ in range(50):
    cur.execute("INSERT INTO students (name, group_id) VALUES (%s, %s)", (fake.name(), random.choice(group_ids)))

for _ in range(5):
    cur.execute("INSERT INTO teachers (name) VALUES (%s)", (fake.name(),))

teacher_ids = range(1, 6)
subjects = ['Math', 'Physics', 'Chemistry', 'Biology', 'Computer Science']
for subject in subjects:
    cur.execute("INSERT INTO subjects (name, teacher_id) VALUES (%s, %s)", (subject, random.choice(teacher_ids)))

student_ids = range(1, 51)
subject_ids = range(1, len(subjects) + 1)
for _ in range(200):
    cur.execute("INSERT INTO grades (student_id, subject_id, grade, date) VALUES (%s, %s, %s, %s)",
                (random.choice(student_ids), random.choice(subject_ids), round(random.uniform(2, 5), 2), fake.date()))

conn.commit()
cur.close()
conn.close()