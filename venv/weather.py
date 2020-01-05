import requests
# from bs4 import BeautifulSoup
import lxml.html as lh
import pandas as pd

url = 'https://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID=51157&Month=11&Day=1&Year=2019&timeframe=2&StartYear=1840&EndYear=2019'
page = requests.get(url)
# soup = BeautifulSoup(page.content, 'html.parser')
doc = lh.fromstring(page.content)

# Parsing data that is stored between <tr>..</tr> of HTML
tr_elems = doc.xpath('//tr')

# print([len(t) for t in tr_elems[:4]])
# print(len(tr_elems))
# print(tr_elems[2].text_content())

# creating empty list
col = []
i = 0

# storing only the first 3 columns since we only need the date & max, min temps
for elem in tr_elems[0]:

    i += 1
    nameOfCol = elem.text_content()
    col.append(nameOfCol)
    if(i>2):
        break
# print(col)

ctr = 0
for j in range(1, len(tr_elems)):
    ctr+=1

    t = tr_elems[j]
    data = t.text_content()
    # print(data[:35])
    data = int(data[:35].strip())
    col[j][1].append(data)

    if(ctr>2):
        break

print(col)


# # storing temperature data from the 2nd row onwards
# for j in range(1, len(tr_elems)):
#     a = tr_elems[j]
#     i = 0
#
#     if (i < 3):
#         for k in a.iterchildren():
#             data = k.text_content()
#             print((float(data.strip())))
#     else:
#         break
#
#     col[i][1].append(data)
#     i+=1
# print(col)


