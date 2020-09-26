from league.league import league
from players import active_week, free_week
import matplotlib.pyplot as plt

weeks = [1,2]

for week in weeks:
    actual = [player.points for player in active_week[week]]
    projected = [player.projected_points for player in active_week[week]]
    free_actual = [player.points for player in free_week[week]]
    free_projected = [player.projected_points for player in free_week[week]]

    plt.scatter(projected, actual, label = 'Drafted')
    plt.scatter(free_projected, free_actual, label = 'Free Agents')

    import numpy as np
    x = np.arange(max(projected))
    y = x
    plt.plot(x,y, label = "Perfect Predictions", color = 'black')

    

    title = f'Week {week} Projected vs. Actual'
    plt.title(title)
    plt.ylabel('Actual Points')
    plt.xlabel('Projected Points')
    plt.savefig(f'{title}.png', bbox_inches = 'tight')
    plt.legend()
    plt.show()
