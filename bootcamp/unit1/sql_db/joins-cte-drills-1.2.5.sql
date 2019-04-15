-- Joins and CTEs
--1. What are the 3 longest trips on rainy days?
--2. Which station is full most often?
--3. Return a list of stations with a count of number of trips
-- starting at that station but ordered by dock count.
--4. (Challenge) What's the length of the longest trip for each day
-- it rains anywhere?

--1. 
WITH rainy as 
(
SELECT 
    DATE(date) rain_date
From 
    weather
WHERE 
    events = 'Rain'
GROUP BY 
    1
) 
SELECT
    t.trip_id,
    t.duration,
DATE(t.start_date)
FROM
    trips t
JOIN
    rainy r
on
    DATE(t.start_date) = r.rain_date
ORDER BY
    duration
DESC
LIMIT 3

--2.
SELECT
    stations.station_id,
    COUNT(*) count_full
FROM
    stations
JOIN
    STATUS
ON
    stations.station_id = status.station_id
WHERE
    status.docks_available = 0
GROUP BY
    stations.station_id
ORDER BY
    count_full
DESC
LIMIT 1
GROUP BY stations.station_id ORDER BY count_full DESC LIMIT 1;

--3.
SELECT
    stations.name,
    stations.dockcount,
    COUNT(*) total_duration
FROM
    stations
JOIN
    trips
ON
    stations.name = trips.start_station
GROUP BY
    stations.name,
    stations.dockcount
ORDER BY
    stations.dockcount
DESC

--4.
WITH rainy as 
(
SELECT 
DATE(date) weather_date
From 
    weather
WHERE
    events = 'Rain'
GROUP BY 1
),
rain_trips as (
SELECT
    trip_id,
    duration,
DATE(trips.start_date) rain_trips_date
FROM
    trips
JOIN
    rainy
on rainy.weather_date = DATE(trips.start_date)
ORDER BY
    duration
DESC    
)
SELECT 
    rain_trips_date,
    max(duration) max_duration
from
    rain_trips
GROUP BY 1
ORDER BY max_duration DESC


