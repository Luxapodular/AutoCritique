import requests 
from bs4 import BeautifulSoup
import re 
import time

print "Starting..."
mainLink = "http://www.artforum.com/words/page_id="
articleLink = "http://www.artforum.com/words/id="
maxPages = 97

# Wait Time between pages in milliseconds. In case they rate limit you. 
waitTime = .1
# *Folder* to save Articles to. 
saveArticlesTo = "artforum"
# *Folder* to save Article Info to. 
saveInfoTo = "artforum/Info/"

reviewExtensions = []

# Go through every page in artforum. 
for i in xrange(maxPages): 
    print "Sleeping..."
    time.sleep(waitTime)
    page = i+1 
    print "Requesting..."
    try: 
        r = requests.get(mainLink + str(page))
    except: 
        print "Error On Request"

    print "Souping..."
    soup = BeautifulSoup(r.content,"lxml") 

    print "Finding..."
    # Reviews have unique id's which are hidden in the images which represent them B) 
    reviewHeads = soup.find_all("a",{"name": re.compile("^img")})

    print "Formatting..."
    for a in reviewHeads:
        try: 
            reviewExtensions.append(a.find_all("img")[0]["item_id"])
        except:
            print "FAILURE : item_id DNE"

    print "Done! \n"

print reviewExtensions

extensionNum = 0; 
for extension in reviewExtensions: 
    time.sleep(waitTime)
    print "Waiting on Article..."

    print "Requesting..."
    r = requests.get(articleLink + extension)

    print "Souping..."
    soup = BeautifulSoup(r.content,"lxml") 

    print "Finding..."
    # Reviews have unique id's which are hidden in the images which represent them B) 
    reviewText = soup.find_all("div",{"class" : "Core"})

    print "Formatting..."
    fullReview = ""
    for r in reviewText:
        for p in r.find_all("p"):
            fullReview += p.text
            fullReview += "\n"


    print "Saving..."
    if (len(fullReview) > 0) :
        try:
            extensionNum += 1
            # Create and store review info. 
            reviewFile = open(("artForumReviews/review%d.txt" % extensionNum), 'w')
            reviewFile.write(fullReview.encode('utf8'))
            reviewFile.close()

        except:
            print "FAILURE : Saving"



