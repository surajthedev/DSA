# Table: Activity

# +--------------+---------+
# | Column Name  | Type    |
# +--------------+---------+
# | player_id    | int     |
# | device_id    | int     |
# | event_date   | date    |
# | games_played | int     |
# +--------------+---------+
# (player_id, event_date) is the primary key (combination of columns with unique values) of this table.
# This table shows the activity of players of some games.
# Each row is a record of a player who logged in and played a number of games (possibly 0) before logging out on someday using some device.
# Write a solution to report the fraction of players that logged in again on the day after the day they first logged in, rounded to 2 decimal places. In other words, you need to determine the number of players who logged in on the day immediately following their initial login, and divide it by the number of total players.

# The result format is in the following example.

 

# Example 1:

# Input: 
# Activity table:
# +-----------+-----------+------------+--------------+
# | player_id | device_id | event_date | games_played |
# +-----------+-----------+------------+--------------+
# | 1         | 2         | 2016-03-01 | 5            |
# | 1         | 2         | 2016-03-02 | 6            |
# | 2         | 3         | 2017-06-25 | 1            |
# | 3         | 1         | 2016-03-02 | 0            |
# | 3         | 4         | 2018-07-03 | 5            |
# +-----------+-----------+------------+--------------+
# Output: 
# +-----------+
# | fraction  |
# +-----------+
# | 0.33      |
# +-----------+
# Explanation: 
# Only the player with id 1 logged back in after the first day he had logged in so the answer is 1/3 = 0.33







# SQL Schema:

# Create table If Not Exists Activity (player_id int, device_id int, event_date date, games_played int)
# Truncate table Activity
# insert into Activity (player_id, device_id, event_date, games_played) values ('1', '2', '2016-03-01', '5')
# insert into Activity (player_id, device_id, event_date, games_played) values ('1', '2', '2016-03-02', '6')
# insert into Activity (player_id, device_id, event_date, games_played) values ('2', '3', '2017-06-25', '1')
# insert into Activity (player_id, device_id, event_date, games_played) values ('3', '1', '2016-03-02', '0')
# insert into Activity (player_id, device_id, event_date, games_played) values ('3', '4', '2018-07-03', '5')


# Pandas Schema:
# data = [[1, 2, '2016-03-01', 5], [1, 2, '2016-03-02', 6], [2, 3, '2017-06-25', 1], [3, 1, '2016-03-02', 0], [3, 4, '2018-07-03', 5]]
# activity = pd.DataFrame(data, columns=['player_id', 'device_id', 'event_date', 'games_played']).astype({'player_id':'Int64', 'device_id':'Int64', 'event_date':'datetime64[ns]', 'games_played':'Int64'})









# Pandas Solution:
import pandas as pd

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    first_login = activity.groupby('player_id')['event_date'].min().reset_index()

    next_day = first_login.copy()
    next_day['event_date'] = next_day['event_date'] + pd.Timedelta(days=1)

    logged_next_day = activity.merge(
        next_day,
        on=['player_id', 'event_date'],
        how='inner'
    )['player_id'].nunique()

    total_players = activity['player_id'].nunique()

    return pd.DataFrame({
        'fraction': [round(logged_next_day / total_players, 2)]
    })