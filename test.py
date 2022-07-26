
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


# Select name, phone, city_id
# from temptable t, cities c
# WHERE t.city = c.CityName


conn = sqlite3.connect('db/database.sqlite')
c = conn.cursor()

# df_players = pd.read_sql(f"Select * from Player p, Player_Attributes pa WHERE p.player_api_id = pa.player_api_id", conn)

# df_players.to_csv('newplayers.csv', index=False)

# df_players = pd.read_sql(f"SELECT * FROM Player LEFT JOIN Player_Attributes ON Player.player_api_id = Player_Attributes.player_api_id WHERE Player.player_api_id != ''", conn)
# df_players.to_csv('newplayers.csv', index=False)



df_leaguee = pd.read_csv('newplayers.csv')

# remove duplicate columns
df_players_new = df_leaguee.loc[~df_leaguee.index.duplicated(),:].copy()
# print(df_players_new.head())

# df_players_new['max_crossing'] = df_players_new.groupby('player_name')['crossing'].transform('max')
# print(df_players_new)

df_players_new = df_players_new.drop_duplicates(subset=['player_name'], keep='first')
# print(df_players_new)

# MAX CROSSING
max_crossing = df_players_new['crossing'].max()
max_finishing = df_players_new['finishing'].max()
max_heading_accuracy = df_players_new['heading_accuracy'].max()
max_short_passing = df_players_new['short_passing'].max()
max_volleys = df_players_new['volleys'].max()
max_dribbling = df_players_new['dribbling'].max()
max_curve = df_players_new['curve'].max()


# MIN CROSSING
min_crossing = df_players_new['crossing'].min()
min_finishing = df_players_new['finishing'].min()
min_heading_accuracy = df_players_new['heading_accuracy'].min()
min_short_passing = df_players_new['short_passing'].min()
min_volleys = df_players_new['volleys'].min()
min_dribbling = df_players_new['dribbling'].min()
min_curve = df_players_new['curve'].min()
print(min_crossing)

# print(df_leaguee.describe())

# print(df_leaguee['height'].mean())
# print(df_leaguee['weight'].mean())



# PROFILE FOR THE MAXIMUM
max_ = df_players_new.loc[df_players_new['crossing'].idxmax()]
print(max_)


# PROFILE FOR THE MINIMUM
min_ = df_players_new.loc[df_players_new['crossing'].idxmin()]
print(min_)