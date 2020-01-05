import json

with open("output.json") as json_data:
    jsonData = json.load(json_data)

# this gives all the dates and time of the tweets
# for i in jsonData:
#     print(i['date&time'])

# to count the number of times "obama" was mentioned in the tweet
for i in jsonData:
    if( "obama" in i['tweetContent'].lower() ):
        print(i)