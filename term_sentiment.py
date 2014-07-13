import sys
import json

scores = {} # initialize an empty dictionary so it's available globally

def dictionary():
    afinnfile = open(sys.argv[1]) # load up AFN-111 dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited
        scores[term] = int(score)  # Convert the score to an integer

def getTextFromTweet():
    tweet_file = open(sys.argv[2]).readlines() # get the file of tweets
    tweets = json.loads(tweet_file[22]) # the first 22 lines of a twitter response are junk    
    for tweet in tweets['statuses']: # loop through the json looking for tweets
        tweet_words = tweet['text'].split() # find the text element and split it into words
        for word in tweet_words:
            if word in scores: # see if a word exists in the scores dict
                nextWord = tweet_words[(tweet_words.index(word) + 1)] # grab the word imediately after it
                if not nextWord in scores: # only include adjacent words that are not in AFN-111
                    print nextWord, scores[word] # print out the nextWord alomg with the score from the original word

def main():
    dictionary()
    getTextFromTweet()

if __name__ == '__main__':
    main()
