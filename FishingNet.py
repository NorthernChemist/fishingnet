# Script for downloading the No Such Thing as a Fish Podcast in mp3 format
# Buy their merch: https://www.nosuchthingasafish.com/

import requests
import feedparser
import os.path

feedURL = 'http://audioboom.com/channels/2399216.rss'

#your location of choice
localDirectory = 'C:/temp/'

rssFeedDict = feedparser.parse(feedURL)

illegalWindowsChars = '<>:"/\|?*'

episodeList = rssFeedDict['entries']

episodeList.reverse()

for episode in episodeList:
    currentTitle = episode['title'] + '.mp3'
    for character in illegalWindowsChars:
        if currentTitle.find(character) !=-1:
            if character == ":":
                currentTitle = currentTitle.replace(character, " -")
            else:
                currentTitle = currentTitle.replace(character, "-") 

    currentURL = episode['media_content'][0]['url']
    currentURL = currentURL.split('?', 1)[0]
    currentTitle = localDirectory + currentTitle
    #obligatory debugging line
    #print(currentTitle)

    #only download new files
    if not os.path.isfile(currentTitle):
        r = requests.get(currentURL, allow_redirects=True)
        open(currentTitle, 'wb').write(r.content)

