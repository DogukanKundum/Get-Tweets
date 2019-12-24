import sys
import codecs
import pandas as pd
UTF8Writer = codecs.getwriter('utf8')
sys.stdout = UTF8Writer(sys.stdout)

if sys.version_info[0] < 3:
    import got
else:
    import got3 as got

def main():
    def printTweet(descr, t):
        dat = pd.DataFrame({'date': [], 'tweet': []})
        for item in t:
            entry = {'date': [item.date], 'tweet': [item.text]}
            dat = dat.append([pd.DataFrame(entry)], ignore_index=True)
        dat.to_csv('xxxx.csv', encoding='utf-8')
        dat.head(10)

    # Example - Get tweets by query search
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('xxxx lang:tr -filter:links').setSince("2019-09-01").setUntil("2019-09-27").setMaxTweets(6)
    tweet = got.manager.TweetManager.getTweets(tweetCriteria)

    printTweet("### Example - Get tweets by query search [europe refugees]", tweet)

if __name__ == '__main__':
    main()
