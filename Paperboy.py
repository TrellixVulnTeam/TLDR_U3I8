import newspaper
from newspaper import Article, Source


class News:
    articles = []

    def __init__(self, url):
        self.newspaper = Source(url)
        self.newspaper.clean_memo_cache()
        self.newspaper.build()
        self.articles = self.newspaper.articles

    def get_news(self, num_of_articles):
        return self.newspaper.articles[:num_of_articles]
