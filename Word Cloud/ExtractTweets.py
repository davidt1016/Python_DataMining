

#Importing Library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import re
import traceback

#Keys and tokens based on my created apps on Twitter
#Enter your access_token, acess_token_secret, consumer_key, and consumer_secret for twitter account
#The code won't be able to run without it and uncomment the following lines 14-17
#access_token 
#access_token_secret 
#consumer_key 
#consumer_secret

#keywords to search for, in this case is COVID-19
tracklist = ['COVID-19']
#Global Variable for counting number of twitters
tweet_count = 0
#Variable for number of tweets data to be extracted from Twitter API
num_Of_tweets = 1000

#Opening files
fil = open("D2.txt" , "w")
#Closing the files
fil.close()

#Class for handling the data streaming from Twitter
class StdOutListener(StreamListener):

	#Extracting data from the Tweeter API
	def on_data(self, data):
		#global variables
		global tweet_count
		global num_Of_tweets
		global stream

		#If the tweet count hasn't reached 1000 tweets yet, continue to load
		if tweet_count < num_Of_tweets:
			try:
				#print(tweet_count, data, '\n')
				#Keeping only the ID and its tweets and write into Text Files
				tweet_data = json.loads(data)
				#Searching pattern with matching pattern of next line
				pattern1 = re.compile(r'\n')
				tweet_txt = pattern1.sub(r'', tweet_data['text'])
				pattern2 = re.compile(r'RT')
				tweet = pattern2.sub(r'', tweet_txt)
				#Open the files in the dedicated file path for writing it in later
				fil = open("/Users/davidteng/Desktop/D2.txt", "a+")
				#Writing into files with first column as ID followed by the actual tweet in the next column
				fil.write(str(tweet_data['id'])+ "\t" + tweet + "\n") 
				#Increment the tweet count by one after each extraction of tweet data
				tweet_count += 1
			#Base exception for any error encountered
			#except BaseException:
				#print("Error:", tweet_count,data)
			#For tracing back the error purposes
			except Exception as error:
				traceback.print_exc()
				print(error)
			return True
		#Completed 1000 tweets extraction, disconnect with Twitter API
		else:
			stream.disconnect()
	#Output the error status from API
	def on_error(self, status):
		print(status)

#Twitter Authentication connection with Twitter Streaming API
l = StdOutListener()
auth=OAuthHandler(consumer_key ,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
stream=Stream(auth, l)


#Search without Query-D1
#stream.sample(is_async=True)
#Keeping only English tweets
#stream.sample(languages=['en'])

#Search with filter Query-COVID-19-D2 and only allow English for D2
stream.filter(track=tracklist)



