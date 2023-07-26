import feedparser

getNumber = int(input("Enter how many RSS feeder URLs you want to check: "))
URLS = []

for i in range(getNumber):
    link = input(f"Enter URL {i+1}: ")
    URLS.append(link)

for URL in URLS:
    feed = feedparser.parse(URL)
    for item in feed['entries']:
        try:
            print ("TITLE: "+item['title']+ "\n" + "LINK: "+item['link']+"\n" + "DESCRIPTION: "+item['description']+"\n")
        except:
            pass


# SOME URLS for example-
# http://rss.cnn.com/rss/cnn_topstories.rss
# http://feeds.nytimes.com/nyt/rss/HomePage
# http://www.washingtonpost.com/rss/
# https://feeds.simplecast.com/54nAGcIl
# https://timesofindia.indiatimes.com/rssfeedstopstories.cms
