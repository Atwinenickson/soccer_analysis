
import pandas as pd
import sqlite3

df_leaguee = pd.read_csv('newplayers.csv')

# remove duplicate columns
df_players = df_leaguee.loc[~df_leaguee.index.duplicated(),:].copy()

df_players_new = df_players.drop_duplicates(subset=['player_name'], keep='first')



df_players_categories = df_players_new.drop(df_players.columns[[0, 1, 2, 3, 4,  7, 8, 9, 10,  13, 14, 15]], axis=1)

df_players_new = df_players_new.drop(df_players.columns[[0, 1, 3, 4,  7, 8, 9, 10,  13, 14, 15]], axis=1)

categories = df_players_categories.columns.values.tolist()
print(categories)

# Max per category
def max_rating(category):
    max_rating_category = df_players_new[category].max()
    print(f"Best rating for category {category}")
    return max_rating_category


best_rating = lambda : [print(max_rating(category)) for category in categories]
best_rating()

print('..............................')


# Min per category
def min_rating(category):
    min_rating_category = df_players_new[category].min()
    print(f"Worst rating for category {category}")
    return min_rating_category


worst_rating = lambda : [print(min_rating(category)) for category in categories]
worst_rating()

print('..............................')


# BEST PLAYER
def best_player_category(category):
    best_player = df_players_new[df_players_new[category]== df_players_new[category].max()]
    print(f"Best player for category {category}")
    return best_player


best_player = lambda : [print(best_player_category(category)) for category in categories]
best_player()

print('..............................')

# WORST PLAYER
def worst_player_category(category):
    worst_player = df_players_new[df_players_new[category]== df_players_new[category].min()]
    print(f"Worst player for category {category}")
    return worst_player

worst_player = lambda : [print(worst_player_category(category)) for category in categories]
worst_player()


birthday = df_players.drop_duplicates(subset=['player_name'], keep='first')
new_birthday = birthday.filter(['player_name','birthday'])

# Players based on age group
# Under20 = epl_df[epl_df['Age'] <=20]
# age20_25 = epl_df[(epl_df['Age'] >20) & (epl_df['Age'] <= 25)]
# age25_30 = epl_df[(epl_df['Age'] >25) & (epl_df['Age'] <=30)]
# Above30 = epl_df[epl_df['Age'] > 30]