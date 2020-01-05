import pandas as pd
import re
import numpy as np
import requests
from bs4 import BeautifulSoup

url = 'http://www.espn.com/mlb/history/leaders/_/breakdown/season/year/2018/start/1'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

# one = soup.find('tr', attrs={'class':'oddrow player-10-33039'})
# for data in one.find_all('td'):
#     print(data.get_text())

# creating a dataframe to get all the column name data same as it is on the website
header = soup.find('tr', attrs={'class':'colhead'})
cols = [col.get_text() for col in header.find_all('td')]

final_df = pd.DataFrame(columns=cols)
# print(final_df)

# now, populating the dataframe with the values
# there is a pattern in the way data is shown on the website, to take advantage of that, we use the
# regular expression's compile command to get all players' data in one go
players = soup.find_all('tr', attrs={'class': re.compile('row player-10-')})
# print(players)
for plyr in players:

    # stats of each player
    stats = [stat.get_text() for stat in plyr.find_all('td')]
    # print(stats)

    # creating a temp dataframe to store each player's data and concatenating it to final_df
    temp_df = pd.DataFrame(stats).transpose()
    # temp_df = pd.DataFrame(stats)
    temp_df.columns = cols
    # print(temp_df)

    final_df = pd.concat([final_df, temp_df], ignore_index=True)

# print(final_df)

### Up until now, we extracted the stats of only 50 players in MLB, but they are 331 players in total
### so now we loop through each url and scrap information from their website

for i in range(1,331,50):

    url = 'http://www.espn.com/mlb/history/leaders/_/breakdown/season/year/2018/start/{}'.format(i)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    players = soup.find_all('tr', attrs={'class': re.compile('row player-10-')})
    # print(players)
    for plyr in players:

        # stats of each player
        stats = [stat.get_text() for stat in plyr.find_all('td')]
        # print(stats)

        # creating a temp dataframe to store each player's data and concatenating it to final_df
        temp_df = pd.DataFrame(stats).transpose()
        # temp_df = pd.DataFrame(stats)
        temp_df.columns = cols
        # print(temp_df)

        final_df = pd.concat([final_df, temp_df], ignore_index=True)

# print(final_df)

# saving the data in a csv file
final_df.to_csv(r'~/Desktop/MLB2018_Stats.csv', index=False, sep=',', encoding='utf-8')