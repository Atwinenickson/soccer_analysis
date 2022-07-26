import pandas as pd
import sqlite3

conn = sqlite3.connect('')
c = conn.cursor()

df = pd.read_sql('SELECT * from wat', conn)

df.to_csv('soccer.csv', index=False)