# This is a jupyter notebook created inside Pycharm to be able to
# learn the basics of the "newspaper" library in Python to extract
# the articles of your choice from a list of millions of articles.

import newspaper
cnn_paper = newspaper.build("http://cnn.com", memoize_articles=False)
print(cnn_paper.size())

# from newspaper import Article

firstArt = cnn_paper.articles[0]
print(cnn_paper.article_urls())
firstArt.download()
firstArt.parse()

print(firstArt.text)

# for article in cnn_paper.articles:
#     print(article.url)

# for categories in cnn_paper.category_urls():
#     print(categories)

