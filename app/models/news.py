class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,source,author,title,description,url,poster):
        self.news_source =source
        self.news_author =author
        self.news_title = title
        self.news_description = description
        self.news_url= url
        self.news_poster= poster