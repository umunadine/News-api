import unittest
from models import news
News = news.News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the news class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News('Engadget','Kendall','The best deals on smartwatches and wearables for Black Friday','We all could use a little help staying active, especially now when many of us are staying home more and more. That’s arguably the most obvious reason to get a smartwatch, but these wearables have grown over the past few years to do other things, too, like pla…','https://www.engadget.com/best-smartwatch-fitness-tracker-wearable-deals-black-friday-2020-161529653.html','"https://o.aolcdn.com/images/dims?resize=1200%2C630&crop=1200%2C630%2C0%2C0&quality=95&image_uri=https%3A%2F%2Fs.yimg.com%2Fos%2Fcreatr-uploaded-images%2F2020-11%2Ff5020a30-1ea9-11eb-8cae-ac66c430ff70&client=amp-blogside-v2&signature=4c7664a2b2b83d232cbf797452daaedfcc340856')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))


if __name__ == '__main__':
    unittest.main()