# from master_frame import df
import pandas as pd
df = pd.read_pickle('./master.pkl')
print(df.iloc[0,:])
from bokeh.plotting import figure, output_file, save
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool
import numpy as np
import bokeh.models.formatters as formatthis

from bokeh.resources import CDN
from bokeh.embed import file_html
# filtering methods for plotting
df['yardage_differential'] = df['RYds/G_x'].astype(float) - df['RYds/G_y'].astype(float) #offense minus defense
df['projected_differential'] = df['Points'] - df['Projected']
filter_df = df

filter_df = df[df['Team_x'] == 'BAL']

# filter_df = filter_df[filter_df['Side'] == 'Defense']

# do a min max norm for rushing yards visualisation
standard = lambda column : [(item-column.min())/(column.max() -  column.min()) for item in column]
# filter_df['yardage_differential'] = standard(filter_df['yardage_differential'].astype(float))
# filter_df =
# print(filter_df.columns)
source = ColumnDataSource(filter_df)
g = figure(plot_height=600, plot_width=700, title="Fantasy Football Player Database")
g.circle(y='Points', x='Opponent_Rank', color = 'Agent Color', source=source, size=8, line_color='black')
g.xgrid.grid_line_alpha = 1
g.xgrid.grid_line_color = 'black'
g.ygrid.grid_line_color = 'black'

hover = HoverTool()

hover.tooltips = [
    ('Name', '@Name'),
    ('Position', '@Position'),
    ('Team', '@Team_x'),
    # ('Opponent Rank', '@Opponent Rank'),
    ('Slot', '@Slot'),
    ('Projected', '@Projected'),
    ('Opponent', '@Opponent'),
    ('Opp Rank', '@Opponent_Rank'),
    ('Week', '@Week')


]

g.add_tools(hover)
# darker lines
# add more

output_file('Fantasy.html')
save(g)