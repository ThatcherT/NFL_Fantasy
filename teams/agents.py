from league.league import league
positions = ['QB', 'RB', 'WR', 'TE', 'D/ST', 'FLEX', 'K']
free_agents_dict = { pos: league.free_agents(position=pos) for pos in positions}
# keys are positions, returns list of player objects