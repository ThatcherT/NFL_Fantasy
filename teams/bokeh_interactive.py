# from master_frame import df
import pandas as pd
df = pd.read_pickle('./master.pkl')
from bokeh.plotting import figure, output_file, save
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool
import numpy as np
import bokeh.models.formatters as formatthis
print(df.columns)
from bokeh.resources import CDN
from bokeh.embed import file_html
# filtering methods for plotting
print(df['Team_x'])
print(df['Opp Join'])
# filter_df = df[df['Slot'] == 'RB']
# filter_df = filter_df[filter_df['Side'] == 'Defense']

# do a min max norm for rushing yards visualisation
standard = lambda column : [(item-column.min())/(column.max() -  column.min()) for item in column]
filter_df['Std_RYds/G'] = standard(filter_df['RYds/G'].astype(float))
# filter_df =
print(filter_df.columns)
source = ColumnDataSource(filter_df)
g = figure(plot_height=600, plot_width=700, title="Fantasy Football Player Database")
g.circle(y='Points', x='Std_RYds/G', color = 'Agent Color', source=source, size=8, line_color='black')
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