import pandas as pd
import sqlite3

conn = sqlite3.connect('db/database.sqlite')
c = conn.cursor()

df = pd.read_sql('SELECT * from Player', conn)

df.to_csv('soccer.csv', index=False)