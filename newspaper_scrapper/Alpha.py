from tldr.TLDR import TLDR
from newspaper_scrapper import Paperboy
from textblob import TextBlob
import time
num_of_articles = 1
cnn = Paperboy.News('http://cnn.com')
articles = cnn.get_news(num_of_articles)
bloblist = []
titles = []
start = time.time()

for i in range(0, num_of_articles):
    article = articles[i]
    article.download()
    article.parse()
    titles.append(article.title)
    bloblist.append(TextBlob(article.text))

for i in range(1, len(bloblist)):
    print("TLDR: ", i, titles[i], '\n')
    summary = TLDR(bloblist[i], bloblist).get_tldr_version(6)
    print(summary, '\n')

print("Total time: ", time.time() - start)
