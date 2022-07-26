
import pandas as pd
import sqlite3

df_leaguee = pd.read_csv('newplayers.csv')

# remove duplicate columns
df_players_new = df_leaguee.loc[~df_leaguee.index.duplicated(),:].copy()

df_players_new = df_players_new.drop_duplicates(subset=['player_name'], keep='first')




categories = ['crossing', 'finishing']

# Max per category
def max_rating(category):
    max_rating_category = df_players_new[category].max()
    return max_rating_category


best_rating = lambda : [print(max_rating(category)) for category in categories]
best_rating()


# Min per category
def min_rating(category):
    min_rating_category = df_players_new[category].min()
    return min_rating_category


worst_rating = lambda : [print(min_rating(category)) for category in categories]
worst_rating()


# BEST PLAYER
def best_player_category(category):
    best_player = df_players_new[df_players_new[category]== df_players_new[category].max()]
    return best_player


best_player = lambda : [print(best_player_category(category)) for category in categories]
best_player()

# WORST PLAYER
def worst_player_category(category):
    worst_player = df_players_new[df_players_new[category]== df_players_new[category].min()]
    return worst_player

worst_player = lambda : [print(best_player_category(category)) for category in categories]
worst_player()

