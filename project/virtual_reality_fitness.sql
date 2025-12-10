SELECT
    user_id,
    COALESCE(
        age,
        (SELECT AVG(age) FROM users WHERE age IS NOT NULL)
    ) AS age,
    COALESCE(
        registration_date,
        '2024-01-01-00-00-000'
    ) AS registration_date,
    COALESCE(
        email,
        'Unknown'
    ) AS email,
    COALESCE(
        CASE
            WHEN LOWER(workout_frequency) IN ('minimal', 'flexible', 'regular', 'maximal')
            THEN LOWER(workout_frequency)
            ELSE 'flexible'
        END,
        'flexible'
    ) AS workout_frequency
FROM
    users;


SELECT
    e.event_id,
    e.user_id,
    e.device_id,
    e.event_time,
    CASE
        WHEN e.game_id IS NOT NULL THEN e.game_id
        WHEN e.game_id IS NULL AND CAST(SUBSTR(e.event_time, 1, 4) AS INTEGER) < 2021
        THEN g.game_id
        ELSE e.game_id
    END AS game_id
FROM
    events AS e
LEFT JOIN
    games AS g ON g.game_type = 'running';

SELECT
    e.user_id,
    e.event_time
FROM
    events AS e
INNER JOIN
    games AS g ON e.game_id = g.game_id
WHERE
    g.game_type = 'biking';



SELECT
    g.game_type,
    g.game_id,
    COUNT(DISTINCT e.user_id) AS user_count
FROM
    events AS e
INNER JOIN
    games AS g ON e.game_id = g.game_id
GROUP BY
    g.game_type,
    g.game_id
HAVING
    g.game_type IS NOT NULL;