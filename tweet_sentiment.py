import sys
import json

scores = {} # initialize an empty dictionary so it's available globally

def dictionary():
    afinnfile = open(sys.argv[1])
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

def getTextFromTweet():
    tweet_file = open(sys.argv[2]).readlines() # get the file of tweets
    tweets = json.loads(tweet_file[22]) # the first 22 lines of a twitter response are junk    
    for tweet in tweets['statuses']: # loop through the json looking for tweets
        tweet_words = tweet['text'].split() # find the text element and split it into words
        for word in tweet_words:
            if word in scores: # see if a word exists in the scores dict
		print tweet['text']
                print 'keyword:', word
		print 'score', scores[word] # if it does, print it out alomg with it's score value
		print
def main():
    dictionary()
    getTextFromTweet()

if __name__ == '__main__':
    main()
