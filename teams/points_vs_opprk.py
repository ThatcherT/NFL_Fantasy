from players import active_week, free_week
import matplotlib.pyplot as plt

weeks = [1, 2]

for week in weeks:
    actual = [player.points for player in active_week[week]]
    opprk = [player.pro_pos_rank for player in active_week[week]]
    free_actual = [player.points for player in free_week[week]]
    free_opprk = [player.pro_pos_rank for player in free_week[week]]

    plt.scatter(opprk, actual, label='Drafted')
    # plt.scatter(free_opprk, free_actual, label='Free Agents')

    import numpy as np

    # x = np.arange(max(projected))
    # y = x
    # plt.plot(x, y, label="Perfect Predictions", color='black')

    title = f'Week {week} Opponent Rank Against Position vs. Points'
    plt.title(title)
    plt.ylabel('Actual Points')
    plt.xlabel('Rank Against Position')
    plt.savefig(f'{title}.png', bbox_inches='tight')
    plt.legend()
    plt.show()