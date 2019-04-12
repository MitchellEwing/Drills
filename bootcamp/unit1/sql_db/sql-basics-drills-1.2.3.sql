--DRILLS:
--1. The IDs and durations for all trips of duration greater than 500, ordered by duration
--2. Every column of the stations table for station id 84.
--3. The min temperatures of all the occurrences of rain in zip 94301.

--1.
SELECT
	trip_id,
	duration
FROM
	trips
WHERE
	duration > 500
ORDER BY duration DESC

--2.
SELECT
	*
FROM
	stations
WHERE
	station_id = 84

--3.
SELECT
	zip,
	mintemperaturef
FROM
	weather
WHERE
	zip = 94301











