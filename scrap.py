import praw
from psaw import PushshiftAPI
import pandas as pd
import datetime as dt
import re 
from pprint import pprint as print



reddit = praw.Reddit(client_id='nsitoMzM8H19pA', client_secret='sx4jlxSsmL6n4NOUt080VZ1dvas', user_agent='Watch Exchange Web Scrapper')
api = PushshiftAPI(reddit)

start_epoch=int(dt.datetime(2017, 1, 1).timestamp())

results = list(api.search_submissions(subreddit='Watchexchange',
                            limit=1))
wts = re.compile('\\[WTS\\]')
price = re.compile(r'[$][\d]+')

testpost = reddit.submission(id=results[0].id)
print(testpost)