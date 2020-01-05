from newspaper import Article

# url = 'https://www.economist.com/britain/2019/12/18/britains-tories-are-the-worlds-most-successful-party-heres-why'

url = 'https://timesofindia.indiatimes.com/india/no-rules-framed-for-all-india-nrc-in-assam-it-was-sc-mandated-pm/articleshow/72930590.cms'

article = Article(url)

article.download()
article.parse()
article.nlp()

# with open("Economist.txt", 'w') as file:
#     file.write(article.text)
#     # file.write(article.publish_date)

with open("TheTimes.txt", 'w', encoding='utf-8', newline='\r\n') as file:
    # file.write(article.authors)
    file.write(article.text)

# print(article.summary)