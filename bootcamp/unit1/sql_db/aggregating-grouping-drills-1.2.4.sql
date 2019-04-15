-- Aggregating and Grouping
--1. What was the hottest day in our data set? Where was that?
--2. How many trips started at each station?
--3. What's the shortest trip that happened?
--4. What is the average trip duration, by end station?

--1. 
SELECT
    date,
    maxtemperaturef,
    zip
FROM
    weather
ORDER BY
    maxtemperaturef
DESC
LIMIT
	1

--2.
SELECT
	start_station,
	count(*) as num_trips
FROM
	trips
	
GROUP BY
	start_station

--3.
SELECT
    trip_id,
	duration
FROM
    trips
ORDER BY
    duration
LIMIT 1

--4.
SELECT
    end_station,
    AVG(duration) as avg_duration
FROM
    trips
GROUP BY
    end_station