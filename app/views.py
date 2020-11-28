# from flask import render_template
# from app import app

# # Views
# @app.route('/')
# def index():

#     '''
#     View root page function that returns the index page and its data
#     '''
#     return render_template('index.html')


from flask import render_template
from app import app
from .request import my_news

@app.route('/')
def index():
    myNewsData =my_news()
    print(myNewsData)
    return render_template('index.html', data=myNewsData)

