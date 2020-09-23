from league.league import league
weeks = [1,2]
matchups_dict = {}
box_dict = {}
for week in weeks:
    matchups_dict.update({week : league.scoreboard(week)})
    box_dict.update({week: league.box_scores(week)})
week1matchups = matchups_dict[1]
week1box = box_dict[1]

teams = []
for matchup in week1matchups:
    teams.append(matchup.home_team)
    teams.append(matchup.away_team)
player_list = []
for team in teams:
    for player in team.roster:
        player_list.append(player)

players = []
for box in week1box:
    players.append(box.home_lineup)
    players.append(box.away_lineup)

print(players)