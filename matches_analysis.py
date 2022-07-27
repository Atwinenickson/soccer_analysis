import pandas as pd


# df_home = pd.read_csv('home_team_matches.csv')
# df_away = pd.read_csv('away_team_matches.csv')
# print(df_home.head())
# print(df_away.head())

# print(df_home.head(2))
# print(df_away.head(2))

# df_away.drop(['season', 'stage', 'date'], axis=1, inplace=True)
# print(df_away.head())


# concantd = df_home.join(df_away)
# print(concantd.head())

# df_head_to_head = concantd.to_csv('head_to_head_matches.csv')

# head_to_head = pd.read_csv('head_to_head_matches.csv')

# total_home_goals = head_to_head['home_team_goal'].sum()
# print(total_home_goals)

# total_away_goals = head_to_head['away_team_goal'].sum()
# print(total_away_goals)


# GET TEAM'S MOST SCORED GOALS FOR A MATCH
# head_to_head = pd.read_csv('head_to_head_matches.csv')

# max_res = head_to_head.groupby('home_team')['home_team_goal'].max().reset_index()
# max_res.columns = ['home_team', 'max_goal']
# print(max_res.head())
# max_res.to_csv('most_goals_per_team.csv')

# GET TEAM'S LESS SCORED GOALS FOR A MATCH
# head_to_head = pd.read_csv('head_to_head_matches.csv')

# min_res = head_to_head.groupby('away_team')['away_team_goal'].min().reset_index()
# min_res.columns = ['away_team', 'min_goal']
# print(min_res.head())
# min_res.to_csv('less_goals_per_team.csv')

# TEAMs THAT SCORED MOST GOALS
# team_max_goals =  pd.read_csv('most_goals_per_team.csv')
# print(team_max_goals[team_max_goals.max_goal == team_max_goals.max_goal.max()])


# TEAMs THAT SCORED LESS GOALS
# team_min_goals =  pd.read_csv('less_goals_per_team.csv')
# print(team_min_goals[team_min_goals.min_goal == team_min_goals.min_goal.min()])


# HOME TEAMS THAT WON(AWAY TEAMS THAT LOST)
# head_to_head = pd.read_csv('head_to_head_matches.csv')
# teams_won = head_to_head[head_to_head['home_team_goal'] > head_to_head['away_team_goal']]
# print(teams_won.head())
# teams_won.to_csv('win_teams.csv')

# HOME TEAMS THAT LOST(AWAY TEAMS THAT WON)
# head_to_head = pd.read_csv('head_to_head_matches.csv')
# teams_lost = head_to_head[head_to_head['home_team_goal'] < head_to_head['away_team_goal']]
# print(teams_lost.head())
# teams_lost.to_csv('loss_teams.csv')

# TEAMS THAT DREW(NO TEAM WON)
# head_to_head = pd.read_csv('head_to_head_matches.csv')
# teams_draw = head_to_head[head_to_head['home_team_goal'] == head_to_head['away_team_goal']]
# print(teams_draw.head())
# teams_draw.to_csv('draw_teams.csv')