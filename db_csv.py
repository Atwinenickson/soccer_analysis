import pandas as pd
import sqlite3

conn = sqlite3.connect('db/database.sqlite')
c = conn.cursor()

# df_players = pd.read_sql('SELECT * from Player', conn)
# df_teams = pd.read_sql('SELECT * from Team', conn)
# df_country = pd.read_sql('SELECT * from Country', conn)
# df_league = pd.read_sql('SELECT * from League', conn)

# df_players.to_csv('players.csv', index=False)
# df_teams.to_csv('teams.csv', index=False)
# df_country.to_csv('countries.csv', index=False)
# df_league.to_csv('leagues.csv', index=False)


df_players = pd.read_csv('players.csv')
df_teams = pd.read_csv('teams.csv')
df_country = pd.read_csv('countries.csv')
df_league = pd.read_csv('leagues.csv')

print(df_country)
print('.........................................')
print(df_teams)
print('.........................................')
print(df_country)
print('.........................................')
print(df_league)