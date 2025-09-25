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