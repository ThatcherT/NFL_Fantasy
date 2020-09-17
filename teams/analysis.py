from league.league import league
# print(league.power_rankings(week = 2))

box_scores = league.box_scores(2) #list of matchups (box score objects contain 2 teams)
# print(box_scores)
my_week1 = box_scores[-2]
print(my_week1.home_team)#team object
print(my_week1.home_score)
print(my_week1.away_score)
print(my_week1.home_lineup)
print(my_week1.away_lineup)
matchups_dict = {matchup: {team: roster for team, in matchup}}