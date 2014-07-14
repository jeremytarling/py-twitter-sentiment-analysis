import sys
import json
from collections import Counter

all_words = []

def getTextFromTweet():
    tweet_file = open(sys.argv[1]).readlines() # get the file of tweets
    tweets = json.loads(tweet_file[22]) # the first 22 lines of a twitter response are junk    
    for tweet in tweets['statuses']: # loop through the json looking for tweets
        tweet_words = tweet['text'].split() # find the text element and split it into words
        all_words.extend(tweet_words) # append each tweets words into a list of all_words
    counts = dict(Counter(all_words)) # turn all_words into a dictt, words as keys, occurences as values
    total = len(counts) # total number of words
    for k,v in counts.items():
        freq = float(v) / float(total)
        print k, round(freq, 5)

def main():
    getTextFromTweet()

if __name__ == '__main__':
    main()
