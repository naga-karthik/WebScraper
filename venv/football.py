import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

# creating urls so that the same structure can be used to scrap data from any league any year
base_url = 'https://understat.com/league/'
leagueName = ['EPL', 'LaLiga', 'Bundesliga']
season = ['2016', '2017', '2018', '2019']

# getting the data for EPL 2019-20 season
url = base_url + leagueName[0] + '/' + season[3]
page = requests.get(url)
soup = BeautifulSoup(page.content, 'lxml')

# since the data is in one of the 'script' tags, we use BeautifulSoup to find them all
scripts = soup.find_all('script')

# the data 'teamsData' is in JSON format, we need to convert it into a python readable format
# this is because the soup converts everything into a string

import json

str_json_obj = ''
for elem in scripts:
    if 'teamsData' in elem.text:
        str_json_obj = elem.text.strip()

# print(str_json_obj)
start = str_json_obj.index("('") + 2
end = str_json_obj.index("')")
json_data = str_json_obj[start:end]
# print(json_data)

json_data = json_data.encode('utf-8').decode('unicode_escape')
# print(json_data)

data = json.loads(json_data)
# print(data.keys())
# print(data['83']['title'])
# print(data['83']['history'])

# # printing json data in a structured json format
# format = json.dumps(data, indent=4, sort_keys=True)
# print(format)

#### getting the team names and putting them in a separate dictionary ####
teams = {}   # empty dictionary; elements of the dictionary are called items
for idx in data.keys():  # json data is in a dictionary form, for each entry, there's a key and its corresponding value
    teams[idx] = data[idx]['title']
# print(teams)

#### printing each column and the values under it
cols = []
vals = []
for idx in data.keys():
    cols = list(data[idx]['history'][0].keys())
    vals = list(data[idx]['history'][0].values())

# print(cols)
# print(vals)

# Getting Arsenal's complete data for 2019/20 season
arsenal_data = []
for row in data['83']['history']:
    arsenal_data.append(list(row.values()))

df = pd.DataFrame(arsenal_data, columns=cols)
# print(df.head(3))

# Getting all teams' data
allTeamsData = {}
for (idx, team) in teams.items():
    teamsData = []
    for row in data[idx]['history']:
        teamsData.append(list(row.values()))

    # update the dataframe
    df = pd.DataFrame(teamsData, columns=cols)
    allTeamsData[team] = df

print(allTeamsData['Liverpool'])