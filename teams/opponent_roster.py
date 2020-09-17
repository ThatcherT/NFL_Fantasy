from league.league import league
opponent_teams = league.teams[1:]
print(opponent_teams)
opponent_dict = {team.team_name: team.roster for team in opponent_teams}
opponent_names = [team.team_name for team in opponent_teams]
print(opponent_names[0], opponent_dict[opponent_names[0]])