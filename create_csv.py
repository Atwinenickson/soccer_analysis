
import pandas as pd
import sqlite3

# conn = sqlite3.connect('db/database.sqlite')
# c = conn.cursor()

# df_players = pd.read_sql(f"SELECT League.name, Country.name FROM League LEFT JOIN Country ON League.country_id = Country.id WHERE League.country_id != ''", conn)

# df_players.to_csv('newleague.csv', index=False)


# df_leaguee = pd.read_csv('newleague.csv')
# print(df_leaguee.head())



# conn = sqlite3.connect('db/database.sqlite')
# c = conn.cursor()

# df_players = pd.read_sql(f"SELECT * FROM Team LEFT JOIN Team_Attributes ON Team.team_api_id = Team_Attributes.team_api_id WHERE Team.team_api_id != ''", conn)

# df_players.to_csv('newteams.csv', index=False)


# df_leaguee = pd.read_csv('newteams.csv')
# print(df_leaguee.head())




# conn = sqlite3.connect('db/database.sqlite')
# c = conn.cursor()

# df_players = pd.read_sql(f"Select * from Player p, Player_Attributes pa WHERE p.player_api_id = pa.player_api_id", conn)

# df_players.to_csv('newplayers.csv', index=False)

# df_players = pd.read_sql(f"SELECT * FROM Player LEFT JOIN Player_Attributes ON Player.player_api_id = Player_Attributes.player_api_id WHERE Player.player_api_id != ''", conn)
# df_players.to_csv('newplayers.csv', index=False)



# conn = sqlite3.connect('db/database.sqlite')
# c = conn.cursor()

# df_players = pd.read_sql(f"SELECT t.team_long_name as home_team, m.season, m.stage, m.date,  m.home_team_goal  FROM Team t JOIN Match m ON t.team_api_id = m.home_team_api_id", conn)

# df_players.to_csv('home_team_matches.csv', index=False)

# df_players = pd.read_sql(f"SELECT t.team_long_name as away_team, m.season, m.stage, m.date,  m.away_team_goal  FROM Team t JOIN Match m ON t.team_api_id = m.away_team_api_id", conn)

# df_players.to_csv('away_team_matches.csv', index=False)


df_home = pd.read_csv('home_team_matches.csv')
df_away = pd.read_csv('away_team_matches.csv')
# print(df_home.head())
# print(df_away.head())

# print(df_home.head(2))
# print(df_away.head(2))

# df_away.drop(['season', 'stage', 'date'], axis=1, inplace=True)
# print(df_away.head())


# concantd = df_home.join(df_away)
# print(concantd.head())

# df_head_to_head = concantd.to_csv('head_to_head_matches.csv')