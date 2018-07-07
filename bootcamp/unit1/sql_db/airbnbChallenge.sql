-- What's the most expensive listing? What else can you tell me about the listing?
SELECT
    name,
    room_type,
    neighbourhood,
    availability_365,
    MAX(price) price
FROM
    listings


-- What neighbordhoods seem to be the most popular?
SELECT
    neighbourhood,
    count(*)
FROM
    listings
GROUP BY 1
ORDER BY 2 DESC


-- What time of year is the cheapest time to go to your city? What about the busiest?
SELECT
    strftime('%m', date(last_review)) month,
    count(*) occurences
FROM
    listings
GROUP BY 1
ORDER BY occurences DESC
