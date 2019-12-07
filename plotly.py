from plotly.offline import plot, iplot

# Connect pandas with plotly
import cufflinks as cf

cf.go_offline()

# import seaborn for data set
import seaborn as sns

dataset = sns.load_dataset('tips')
dataset.head()

# Show iplot in Pycharm
dataset2 = dataset[['total_bill', 'tip', 'size']]
plot(dataset2.iplot(asFigure=True))

# Bar plot of groups of different time and sex combination
plot(dataset.iplot(kind='bar', x=['time', 'sex'], y='total_bill', asFigure=True))

# Vertical bar plot of mean of each column
plot(dataset.mean().iplot(kind='bar', asFigure=True))

# Horizontal bar plot of mean of each column
plot(dataset.mean().iplot(kind='barh', asFigure=True))

# Scatter plot
plot(dataset.iplot(kind='scatter', x='total_bill', y='tip', mode='markers', asFigure=True))

# Box plot
plot(dataset2.iplot(kind='box', asFigure=True))

# Histogram
plot(dataset['total_bill'].iplot(kind='hist', bins=25, asFigure=True))

# Scatter matrix plot
plot(dataset2.scatter_matrix(asFigure=True))

# Spread plot
plot(dataset[['total_bill', 'tip']].iplot(kind='spread', asFigure=True))

# 3D plot
plot(dataset2.iplot(kind='surface', colorscale='rdylbu', asFigure=True))

# Geographical plots of USA
import chart_studio.plotly as py
import plotly.graph_objs as go
from plotly.offline import plot, iplot
import pandas as pd
import plotly.io as pio

pio.renderers.default = 'browser'

map_data = dict(type='choropleth',
                locations=['MI', 'CO', 'FL', 'IN'],
                locationmode='USA-states',
                colorscale='Portland',
                text=['Michigan', 'Colorado', 'Florida', 'Indiana'],
                z=[1.0, 2.0, 3.0, 4.0],
                colorbar=dict(title='USA States'))
map_layout = dict(geo={'scope': 'usa'})
map_actual = go.Figure(data=[map_data], layout=map_layout)
map_actual.show()
iplot(map_actual, filename='figure2.html')

df = pd.read_csv('bea-gdp-by-state.csv')
df.head()

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

df['abbrev'] = df['Area'].map(us_state_abbrev)

df.head()

map_data = dict(type='choropleth',
                locations=df['abbrev'],
                locationmode='USA-states',
                colorscale='Reds',
                text=df['Area'],
                marker=dict(line=dict(color='rgb(255, 0, 0)', width=2)),
                z=df['2017'],
                colorbar=dict(title='GDP Per Capita - 2017'))
map_layout = dict(title='USA States GDP Per Capita - 2017',
                  geo=dict(scope='usa',
                           showlakes=True,
                           lakecolor='rgb(85, 173, 240)'))
map_actual = go.Figure(data=[map_data], layout=map_layout)
plot(map_actual, filename='figure3.html')
map_actual.show()
iplot(map_actual)

# Geographical maps of the world
df = pd.read_csv('world_pop.csv')
df.head()

map_data = dict(
                type='choropleth',
                locations=df['Country Code'],
                colorscale='Portland',
                z=df['2016'],
                text=df['Country'],
                colorbar={'title': 'World Population 2016'})

map_layout = dict(title='World Population 2016', geo=dict(showframe=False))

map_actual = go.Figure(data=[map_data], layout=map_layout)

plot(map_actual, filename='figure4.html')
