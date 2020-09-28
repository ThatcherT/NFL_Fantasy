# The goal is to associate players with the team they oppose
# That way, I can look at averaged previous season stats

from league.league import league
weeks = [1,2,3]
matchups_dict = {}
box_dict = {}

# print(league.player_map) # retunrs dict of all player names with unique id as key
# Dak = league.player_info('Dak Prescott')

active_week = {} # dict of active players where each key is a week and value is list of players
free_week = {} # same but for free agents

for week in weeks:

    matchups_dict.update({week : league.scoreboard(week)})
    box_dict.update({week: league.box_scores(week)})

    free_agents = league.free_agents(week, size=500)
    week_matchups = matchups_dict[week]
    week_box = box_dict[week]

    teams = []
    for matchup in week_matchups:
        teams.append(matchup.home_team)
        teams.append(matchup.away_team)
    player_list = []
    for team in teams:
        for player in team.roster:
            player_list.append(player)

    active_players = []
    for box in week_box:
        [active_players.append(player) for player in box.home_lineup]
        [active_players.append(player) for player in box.away_lineup]

    active_week.update({week: active_players})
    free_week.update({week: free_agents})
        # print(box.away_lineup[-2].slot_position)


team_dict = {'ARI':	'Arizona Cardinals',
'ATL'	:'Atlanta Falcons',
'BAL':	'Baltimore Ravens',
'BUF'	:'Buffalo Bills',
'CAR':	'Carolina Panthers',
'CHI':	'Chicago Bears',
'CIN':	'Cincinnati Bengals',
'CLE':	'Cleveland Browns',
'DAL'	:'Dallas Cowboys',
'DEN'	:'Denver Broncos',
'DET':	'Detroit Lions',
'GB'	:'Green Bay Packers',
'HOU'	:'Houston Texans',
'IND'	:'Indianapolis Colts',
'JAX':	'Jacksonville Jaguars',
'KC':	'Kansas City Chiefs',
'LAC'	:'Los Angeles Chargers',
'LAR'	:'Los Angeles Rams',
'LV'	:'Las Vegas Raiders',
'MIA':	'Miami Dolphins',
'MIN':	'Minnesota Vikings',
'NE':	'New England Patriots',
'NO':	'New Orleans Saints',
'NYG':	'New York Giants',
'NYJ':	'New York Jets',
'PHI':	'Philadelphia Eagles',
'PIT':	'Pittsburgh Steelers',
'SEA':	'Seattle Seahawks',
'SF'	:'San Francisco 49ers',
'TB':	'Tampa Bay Buccaneers',
'TEN':	'Tennessee Titans',
'WAS':'Washington Football Team'}