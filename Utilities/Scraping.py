import requests 
from bs4 import BeautifulSoup

print "Starting..."
mainLink = "http://www.artinamericamagazine.com"
reviewTableLink = "http://localhost:8000/aia.html"

# *Folder* to save Articles to. 
saveArticlesTo = "aia/Articles/"
# *Folder* to save Article Info to. 
saveInfoTo = "aia/Info/"

reviewExtensions = []

print "Requesting..."
r = requests.get(reviewTableLink)

print "Souping..."
soup = BeautifulSoup(r.content,"lxml") 

print "Finding..."
reviewHeads = soup.find_all("article", {"class": "reviews-entry"})

print "Formatting..."
for article in reviewHeads : 
	reviewExtensions.append(article.contents[1]['href'])

for i in xrange(4):

	# Pull Articles using extensions from main page. 
	newRequest = requests.get(reviewExtensions[i])

	reviewSoup = BeautifulSoup(newRequest.content,"lxml")

	reviewBody = reviewSoup.find_all("article")

	reviewText = reviewBody[0].text

	# Find and split article by point of Advertisment. 
	start = reviewText.find("Advertisement")
	if (start != -1):
		articleInfo = reviewText[:start]
		articleBody = reviewText[start+len("Advertisement"):]

		# Create and store article info. 
		infoFile = open(("{0}Info/{1}-info.txt".format(saveTo, i)), 'w')
		infoFile.write(articleInfo.encode('utf8'))
		infoFile.close()

		# Create and store article body. 
		articleFile = open(("{0}Articles/{1}-article.txt".format(saveTo, i)), 'w')
		articleFile.write(articleBody.encode('utf8'))
		articleFile.close()
	else:
		print " 'Advertisement' not found in article {0}".format(i)




