SELECT sub.name AS subject_name
FROM subjects sub
JOIN grades g ON sub.id = g.subject_id
WHERE g.student_id = 23 AND sub.teacher_id = 1;