import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID=51157&Month=11&Day=1&Year=2019&timeframe=2&StartYear=1840&EndYear=2019'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'lxml')

table = soup.find('div', attrs={'id': 'dynamicDataTable'})

new_table = pd.DataFrame(columns=range(0,len(table)), index=[0])

row_mark = 0
for rows in table.find_all('tr'):
    # print(rows)
    col_mark = 0
    cols = rows.find_all('td')
    for col in cols:
        print(col.get_text())
        new_table.iat[row_mark, col_mark] = col.get_text()
        col_mark += 1
    row_mark +=1

new_table
