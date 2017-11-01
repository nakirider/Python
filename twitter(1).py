##############################################
#########                           ##########
#########   TWITTER STREAMING API   ##########
#########                           ##########
##############################################
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os
path='C:\\Users\\dehmamy_local\\Dropbox\\Groningen Courses\\Data Science Methods\\Slides\\'
os.chdir(path)
# os.getcwd()

##### This part is important to loading the required modules
##### These modules are "extensions" to the basic Python language,
##### and are constantly updated by the programming community.
# First install tweepy from anaconda console by typing "pip install tweepy"
# The Twitter "library" we'll be using is called tweepy...
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Variables that contains the user credentials to access Twitter API 
# register a new "App" under your Twitter account, and put in
# your credentials below.

access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""

# Define a list of trackable hash tags or character strings
# that you would like to get data on.

#tracking = ['#DWDD', '#NOS', '#Nederland', '#Obama']
#tracking = ['#catalonia', '#spain', '#Trump', '#JCPOA', '#northkorea']
tracking = ['#wehkamp']

# This part is responsible of getting the data, and printing the data.
# It's a basic listener , printing tweets to the output console (stdout).
class StdOutListener(StreamListener):
    def on_data(self, data):
        print data
        return True
    def on_error(self, status):
        print status

# This guy will be called when you launch the script
if __name__ == '__main__':
    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    #This line filter Twitter Streams to capture data by the keywords you defined earlier
    stream.filter(track=tracking)
