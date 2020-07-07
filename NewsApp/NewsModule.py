from requests import get
from datetime import datetime

class News:

    def __init__(self, type = 'bitcoin', limit = 10):
        self.newsType = {
            'bitcoin': 'http://newsapi.org/v2/everything?q=bitcoin&amp&from=2020-05-10&amp&sortBy=publishedAt&amp&apiKey=5088b37404fa417bb5631543b72915d5',
            'business headlines': 'http://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=5088b37404fa417bb5631543b72915d5',
            'tech headlines': 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=5088b37404fa417bb5631543b72915d5',
            'wall street journal': 'http://newsapi.org/v2/everything?domains=wsj.com&apiKey=5088b37404fa417bb5631543b72915d5',
            'apple headlines': f'http://newsapi.org/v2/everything?q=apple&from={News.yesterday()}&to={News.yesterday()}&sortBy=popularity&apiKey=5088b37404fa417bb5631543b72915d5'
        }
        self.response = get(self.newsType[type.lower()]).json()['articles'][0:limit]

    @staticmethod
    def yesterday():
        return f'{datetime.now().year}-{datetime.now().month}-{datetime.now().day - 1}'

if __name__ == '__main__':
    news = News(type='business headlines')
    for news in news.response:
        print(news['urlToImage'])