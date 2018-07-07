WITH
    locations
AS (
    SELECT
        city,
        AVG(lat) lat,
        AVG(long) long
    FROM
        stations
    GROUP BY 1
)
SELECT
    l.city,
    l.lat,
    l.long,
    COUNT(*)
FROM
    locations l
JOIN
    stations s
ON
    l.city = s.city
JOIN
    trips t
ON
    t.start_station = s.name
GROUP BY 1