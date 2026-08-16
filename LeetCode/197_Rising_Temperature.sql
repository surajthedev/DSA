-- Table: Weather

-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | id            | int     |
-- | recordDate    | date    |
-- | temperature   | int     |
-- +---------------+---------+
-- id is the column with unique values for this table.
-- There are no different rows with the same recordDate.
-- This table contains information about the temperature on a certain day.
 

-- Write a solution to find all dates' id with higher temperatures compared to its previous dates (yesterday).

-- Return the result table in any order.

-- The result format is in the following example.

 

-- Example 1:

-- Input: 
-- Weather table:
-- +----+------------+-------------+
-- | id | recordDate | temperature |
-- +----+------------+-------------+
-- | 1  | 2015-01-01 | 10          |
-- | 2  | 2015-01-02 | 25          |
-- | 3  | 2015-01-03 | 20          |
-- | 4  | 2015-01-04 | 30          |
-- +----+------------+-------------+
-- Output: 
-- +----+
-- | id |
-- +----+
-- | 2  |
-- | 4  |
-- +----+
-- Explanation: 
-- In 2015-01-02, the temperature was higher than the previous day (10 -> 25).
-- In 2015-01-04, the temperature was higher than the previous day (20 -> 30).








-- SQL Schema:
-- Create table If Not Exists Weather (id int, recordDate date, temperature int)
-- Truncate table Weather
-- insert into Weather (id, recordDate, temperature) values ('1', '2015-01-01', '10')
-- insert into Weather (id, recordDate, temperature) values ('2', '2015-01-02', '25')
-- insert into Weather (id, recordDate, temperature) values ('3', '2015-01-03', '20')
-- insert into Weather (id, recordDate, temperature) values ('4', '2015-01-04', '30')







-- Pandas Schema:
-- data = [[1, '2015-01-01', 10], [2, '2015-01-02', 25], [3, '2015-01-03', 20], [4, '2015-01-04', 30]]
-- weather = pd.DataFrame(data, columns=['id', 'recordDate', 'temperature']).astype({'id':'Int64', 'recordDate':'datetime64[ns]', 'temperature':'Int64'})






-- SQL Solution:
SELECT w1.id
FROM Weather w1
JOIN Weather w2
    ON DATEDIFF(w1.recordDate, w2.recordDate) = 1
WHERE w1.temperature > w2.temperature;






-- Pandas Solution:
weather = weather.sort_values('recordDate')

weather['prev_temp'] = weather['temperature'].shift(1)
weather['prev_date'] = weather['recordDate'].shift(1)

result = weather[
    ((weather['recordDate'] - weather['prev_date']).dt.days == 1) &
    (weather['temperature'] > weather['prev_temp'])
][['id']]