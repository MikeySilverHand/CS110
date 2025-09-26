import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#line graph
gas = pd.read_csv('Private/gas_prices.csv')

plt.figure(figsize=(8, 5))

plt.title('Gas Prices Over Time (in USD)', fontdict={'fontweight': 'bold', 'fontsize': 18})

plt.plot(gas['Year'], gas['USA'], 'b.-', label='United States')
plt.plot(gas['Year'], gas['Canada'], 'r.-', label='Canada')
plt.plot(gas['Year'], gas['South Korea'], 'g.-', label='South Korea')
plt.plot(gas['Year'], gas['Australia'], 'y.-', label='Australia')

#Another way to plot many values!
# countries_to_look_at = ['Australia', 'USA', 'Canada', 'South Korea']
# for country in gas:
#     if country in countries_to_look_at:
#         plt.plot(gas['Year'], gas[country], marker='.')

plt.xticks(gas['Year'][::3].tolist()+[2011])

plt.xlabel('Year')
plt.ylabel('US Dollars')

plt.legend()

plt.savefig('Gas_price_figure.png', dpi=300)

plt.show()

#Load Fifa Data
fifa = pd.read_csv('Private/fifa_data.csv')

#Histograms
bins = [40, 50, 60, 70, 80, 90, 100]

plt.hist(fifa['Overall'], bins=bins, color='#abcdef')

plt.xticks(bins)

plt.ylabel('Number of Players')
plt.xlabel('Skill Level')
plt.title('Distribution of Player Skills in FIFA 2018')

plt.show()

#Pychart 1
left = fifa.loc[fifa['Preferred Foot'] == 'Left'].count().iloc[0]
right = fifa.loc[fifa['Preferred Foot'] == 'Right'].count().iloc[0]

labels = ['Left', 'Right']
colors = ['#abcdef', "#e02517"]

plt.pie([left, right], labels = labels, colors = colors, autopct='%.2f %%')

plt.title('Foot Preference of FIFA Players')

plt.show()

#Pychart2
fifa.Weight = [int(x.strip('lbs')) if type(x)==str else x for x in fifa.Weight]

plt.style.use('ggplot')#specific style

light = fifa.loc[(fifa.Weight < 125)].count().iloc[0]
light_medium = fifa.loc[(fifa.Weight >= 125) & (fifa.Weight < 150)].count().iloc[0]
medium = fifa.loc[(fifa.Weight >= 150) & (fifa.Weight < 175)].count().iloc[0]
medium_heavy = fifa.loc[(fifa.Weight >= 175) & (fifa.Weight < 200)].count().iloc[0]
heavy = fifa.loc[(fifa.Weight >= 200)].count().iloc[0]

weights = [light, light_medium, medium, medium_heavy, heavy]

labels = ['Under 125', '125-150', '150-175', '175, 200', 'Over 200']

explode = (.4, .1, 0, 0, .4)

plt.title('Weight Distribution of FIFA Players (in lbs)')

plt.pie(weights, labels=labels, autopct='%.2f %%', pctdistance=0.8, explode=explode)

plt.show()

#Box and Whiskers Chart
plt.style.use('default')

plt.figure(figsize=(5, 8))

barcelona = fifa.loc[fifa.Club == 'FC Barcelona']['Overall']
madrid = fifa.loc[fifa.Club == 'Real Madrid']['Overall']
revs = fifa.loc[fifa.Club == 'New England Revolution']['Overall']

labels = ['FC Barcelona', 'Real Madrid', 'NE Revolution']

boxes = plt.boxplot([barcelona, madrid, revs], tick_labels=labels, patch_artist=True, medianprops={'linewidth':2})

for box in boxes['boxes']:
    #set edge color
    box.set(color='#4286f4', linewidth=2)

    #Change fill color
    box.set(facecolor='#e0e0e0')

plt.title('Professional Soccer Team Comparison')

plt.ylabel('FIFA Overall Rating')

plt.show()