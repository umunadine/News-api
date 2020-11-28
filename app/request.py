from app import app
import urllib.request,json
from .models import news

News = news.News

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the movie base url
base_url = app.config["NEWS_API_BASE_URL"]

def my_news():
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = []

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
             

            # news_results = process_results(news_results_list)


            for item in news_results_list:
                source = item.get('source')
                author = item.get('author')
                title = item.get('title')
                description = item.get('description')
                url = item.get('url')
                poster = item.get('urlToImage')
                publishedAt=('publishedAt')
                content=item.get('content')

                # if poster:
                news_object = News(source,author,title,description,url,poster,publishedAt,content)
                news_results.append(news_object)

        return news_results



