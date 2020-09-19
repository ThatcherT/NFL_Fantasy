from league.league import league
teams = league.teams
my_team = teams[0]
team_name = my_team.team_name
# cockrell
roster = my_team.roster
# list of players
opponent_teams = league.teams[1:]
print(opponent_teams)
opponent_dict = {team.team_name: team.roster for team in opponent_teams}
opponent_names = [team.team_name for team in opponent_teams]
print(opponent_names[0], opponent_dict[opponent_names[0]])
print(roster)
print(league.teams[0].__dict__)