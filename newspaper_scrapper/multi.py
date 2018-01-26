import newspaper
import threading
import time
import textblob
from tldr import TLDR
# Attempting to speed up the program using multi threading
start = time.time()
cnn = newspaper.Source('http://cnn.com')
cnn.clean_memo_cache()
cnn.build()
urls = cnn.article_urls()
titles = []
articles = []

# TODO The inefficiency stems from TLDR, not newspaper!
for k in range(5):
    arctic = newspaper.Article(urls[k])
    arctic.build()
    titles.append(arctic.title)
    articles.append(textblob.TextBlob(arctic.text))
    print(titles[k], '\n', arctic.text)


def summarize(m):
    print("Start time: ", time.time())
    summary = TLDR.TLDR(articles[m], articles)
    print("Summary: ", m)
    print('\n', "Title:", titles[m], '\n')
    print(summary.get_tldr_version(5))


del articles[0]
del titles[0]
threads = []

for t in range(4):
    thread = threading.Thread(target=summarize(t))
    threads.append(thread)

threads[0].start()
threads[1].start()
threads[2].start()
threads[3].start()


final = time.time()
total = final - start
print("Total time: ", total)
