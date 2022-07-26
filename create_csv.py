
import pandas as pd
import sqlite3

conn = sqlite3.connect('db/database.sqlite')
c = conn.cursor()

df_players = pd.read_sql(f"SELECT League.name, Country.name FROM League LEFT JOIN Country ON League.country_id = Country.id WHERE League.country_id != ''", conn)

df_players.to_csv('newleague.csv', index=False)


df_leaguee = pd.read_csv('newleague.csv')
print(df_leaguee.head())



conn = sqlite3.connect('db/database.sqlite')
c = conn.cursor()

df_players = pd.read_sql(f"SELECT * FROM Team LEFT JOIN Team_Attributes ON Team.team_api_id = Team_Attributes.team_api_id WHERE Team.team_api_id != ''", conn)

df_players.to_csv('newteams.csv', index=False)


df_leaguee = pd.read_csv('newteams.csv')
print(df_leaguee.head())




conn = sqlite3.connect('db/database.sqlite')
c = conn.cursor()

df_players = pd.read_sql(f"Select * from Player p, Player_Attributes pa WHERE p.player_api_id = pa.player_api_id", conn)

df_players.to_csv('newplayers.csv', index=False)

df_players = pd.read_sql(f"SELECT * FROM Player LEFT JOIN Player_Attributes ON Player.player_api_id = Player_Attributes.player_api_id WHERE Player.player_api_id != ''", conn)
df_players.to_csv('newplayers.csv', index=False)
