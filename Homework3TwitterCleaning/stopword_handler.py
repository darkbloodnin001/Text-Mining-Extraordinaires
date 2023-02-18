import pandas as pd
import string
import numpy as np
import nltk
from nltk.corpus import stopwords

# load stopwords
stop_words = stopwords.words('english')

# load scraped data into dataframe
df = pd.read_csv("all_tweets_group_4.csv", usecols = ['url','date','content','id','user','reply count','retweet count',
                                                      'like count','quote count','conversation id','language','source','coordinates'])

# check for nulls to avoid problems with stopword removal
df = df[df['content'].notnull()]

# remove stopwords
df['content'] = df['content'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop_words)]))

# export to path
df.to_csv(path_or_buf=f"new_all_tweets.csv")

