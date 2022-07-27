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


# HOME TEAM SEASONAL PERFORMANCE
# head_to_head = pd.read_csv('head_to_head_matches.csv')
# home_teams_per_season_max = head_to_head.groupby(['home_team', 'season'])['home_team_goal'].max().reset_index()
# home_teams_per_season_min = head_to_head.groupby(['home_team', 'season'])['home_team_goal'].min().reset_index()
# print(home_teams_per_season_max.head())
# print(home_teams_per_season_min.head())

# AWAY TEAM SEASONAL PERFORMANCE
# head_to_head = pd.read_csv('head_to_head_matches.csv')
# away_teams_per_season_max = head_to_head.groupby(['away_team', 'season'])['away_team_goal'].max().reset_index()
# away_teams_per_season_min = head_to_head.groupby(['away_team', 'season'])['away_team_goal'].min().reset_index()
# print(away_teams_per_season_max.head())
# print(away_teams_per_season_min.head())

# TEAMS THAT PLAYED EACH OTHER SEASONALY
# HOME TEAM SEASONAL PERFORMANCE
# head_to_head = pd.read_csv('head_to_head_matches.csv')
# seasonal_games = head_to_head.groupby(['home_team', 'away_team', 'season', 'home_team_goal', 'away_team_goal'])['home_team_goal', 'away_team_goal'].apply(list)
# print(seasonal_games.head())
# seasonal_games.to_csv('seasonal_games.csv')


# head_to_head = pd.read_csv('head_to_head_matches.csv')
# home_seasonal_games = head_to_head.groupby(['home_team', 'season'])['home_team_goal'].sum().reset_index(name='total_home_goals')
# away_seasonal_games = head_to_head.groupby(['away_team', 'season'])['away_team_goal'].sum().reset_index(name='total_away_goals')
# print(home_seasonal_games.head())
# print(away_seasonal_games.head())


# TOTAL GOALS PER SEASON
# home_seasonal_games['TotalGoals'] = home_seasonal_games['total_home_goals'] + away_seasonal_games['total_away_goals']
# print(home_seasonal_games.head())
# home_seasonal_games.to_csv('total_goals_per_season.csv')

# Maximum goals all seasons
# maxim_goals = pd.read_csv('total_goals_per_season.csv')
# maxim_goals_scored = maxim_goals['TotalGoals'].max()
# print(maxim_goals_scored)

# Team with most goals
# print(maxim_goals[maxim_goals['TotalGoals'] == maxim_goals['TotalGoals'].max()])

# Team with most home goals
# print(maxim_goals[maxim_goals['total_home_goals'] == maxim_goals['total_home_goals'].max()])