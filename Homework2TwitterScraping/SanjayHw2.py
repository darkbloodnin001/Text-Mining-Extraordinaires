import snscrape.modules.twitter as sntwitter
import pandas as pd

##get_100_Tweets(twitter_handle) definition


def get_100_tweets(twitter_handle):
	start = '2019-01-01'  #YYYY-MM-DD   (just starting far back enough to ensure there are 100)
	end = '2023-02-03'  #YYYY-MM-DD

	query = "(from:{}) until:{} since:{}".format(twitter_handle, end, start)
	tweets = []
	limit = 100

	for tweet in sntwitter.TwitterSearchScraper(query).get_items():

		if len(tweets) == limit:
			break
		else:
			tweets.append([
			 tweet.url, tweet.date, tweet.rawContent, tweet.id, tweet.user.username,
			 tweet.replyCount, tweet.retweetCount, tweet.likeCount, tweet.quoteCount,
			 tweet.conversationId, tweet.lang, tweet.source, tweet.coordinates
			])
	return tweets


##Scraping 100 tweets from @ddockett and @Danica Patrick
##-----------------------------------------

twitter_handles = ['ddockett', 'DanicaPatrick']
all_tweets = []

for handle in twitter_handles:
	all_tweets += get_100_tweets(handle)

reggie_dwyane_tweets = pd.DataFrame(all_tweets,
                                    columns=[
                                     'url', 'date', 'content', 'id', 'user',
                                     'replyCount', 'retweetCount', 'likeCount',
                                     'qouteCount', 'conversationId', 'lang',
                                     'source', 'coordinates'
                                    ])
reggie_dwyane_tweets.to_csv('SanjayTweets.csv', mode='a')
