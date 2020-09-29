from league.league import league
from players import active_week, free_week, weeks, team_dict
import numpy as np

# the goal of this is to obtain a dataframe for which
# the following columns are present
# player, points, projected, opponent and opponent metrics, free/drafted bool


# lst = ['one','two','three']
# lst1 = [1, 2, 3]
# print(list(zip(lst, lst1)))

for week in weeks:
    active_players = active_week[week]  # list of players who are drafted
    free_players = free_week[week]

    total_players = active_week[week]
    [total_players.append(free_player) for free_player in free_players]

    name = [player.name for player in total_players]
    # id = [player.playerID for player in total_players]
    position = [player.position for player in total_players]
    # injury = [player.injured for player in total_players]
    team = [player.proTeam for player in total_players]
    opponent = [player.pro_opponent for player in total_players]
    opprk = [player.pro_pos_rank for player in total_players]
    slot = [player.slot_position for player in total_players]
    points = [player.points for player in total_players]
    projected = [player.projected_points for player in total_players]
    WEEK = [week for player in total_players]

    # percent_played = [player.game_played for player in total_players]
    # print(opponent)
    # print(team)
    # print(percent_played)

    # names = [player.name for player in ]
    import pandas as pd

    columns = ['Name', 'Points', 'Position', 'Team', 'Opponent', 'Opponent_Rank', 'Slot', 'Projected', 'Week']
    if week == 1:

        df = pd.DataFrame(list(zip(name, points, position, team, opponent, opprk, slot, projected, WEEK)),
                          columns=columns)
    else:

        df2 = pd.DataFrame(list(zip(name, points, position, team, opponent, opprk, slot, projected, WEEK)),
                           columns=columns)

        df = df.append(df2)
df = df[df['Team'] != 'None']
df = df[df['Opponent'] != 'None']
# filter to remove free agents in league

# Create color system so you can call on this column when plotting with Bokeh (if want to see FA)
df['Agent Color'] = np.where(df['Slot'] != 'FA', 'Red', 'Green')
df['Agent Color'] = np.where(df['Slot'] == 'BE', 'Blue', df['Agent Color'])


# Update Names to Current
df['Team'] = np.where(df['Team'] == 'OAK', 'LV', df['Team'])
df['Team'] = np.where(df['Team'] == 'WSH', 'WAS', df['Team'])
df['Opponent'] = np.where(df['Opponent'] == 'OAK', 'LV', df['Opponent'])
df['Opponent'] = np.where(df['Opponent'] == 'WSH', 'WAS', df['Opponent'])

# print(df['Team'])
df_hist = pd.read_pickle('../Scrape/Historical.pkl')
# df_hist['Abbr'] = np.where(df['Team'])
# TODO Fix opponent and team join
df['Team Join'] = [team_dict[team] for index, team in df['Team'].items()]
df['Opp Join'] = [team_dict[opp] for index, opp in df['Opponent'].items()]


hist_2019 = df_hist[df_hist['Year'] == 2019]
histd_2019 = hist_2019[hist_2019['Side'] == 'Defense']
histo_2019 = hist_2019[hist_2019['Side'] == 'Offense']
df = pd.merge(df, histo_2019, left_on = 'Team Join', right_on = 'Team')
df = pd.merge(df, histd_2019, left_on = 'Opp Join', right_on = 'Team')
print(df.iloc[0,:])
df.to_pickle('./master.pkl')