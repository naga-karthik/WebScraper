from bs4 import BeautifulSoup
import requests
import json

url = 'http://ethans_fake_twitter_site.surge.sh/'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")
# print(content)
dataArray = []  # to store all the data

# allTweetsText = content.findAll('p', attrs={"class": "content"})
# print(allTweetsText)
# allLikes = content.findAll("p", attrs={"class": "likes"})

# what the following line does is it looks through the raw HTML data in the "content" variable and searches for all the
# headers starting with 'p'. But, what the "attrs" does is it specifies to look for classes that only have
# "content" data in them and return only that. So, we need to specify more and more tags and their attributes in order
# to get the exact information we want. The findAll returns in HTML format only. The ".text" method helps to only get
# the text and discarding all the HTML jargon.
# for tweet in content.findAll('p', attrs={'class': "content"}):
#     print(tweet.text.encode('utf-8'))

# if we look at the HTML structure on the website, we can see that the all the necessary info is in 'div' and the class
# 'tweetcontainer'. We can loop through all such classes and extract the required information.
for data in content.findAll('div', attrs={"class": 'tweetcontainer'}):

    dataObj = {"author": data.find('h2', attrs={"class": "author"}).text,
               "tweetContent": data.find('p', attrs={"class": 'content'}).text,
               "date&time": data.find('h5', attrs={"class": 'dateTime'}).text,
               "likes": data.find('p', attrs={"class": 'likes'}).text,
               "shares": data.find('p', attrs={"class": 'shares'}).text,
               }
    dataArray.append(dataObj)

#### Storing data in a JSON format for easy reading ######
with open('output.json', 'w', encoding='utf-8') as file:
        line = json.dumps(dataArray) + '\n'
        file.write(line)

