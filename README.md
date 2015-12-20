# AutoCritique

Auto Critique is a piece of software which aims to automatically generate critiques for visual imagery. To accomplish this, I'll be utilizing image recognition software to generate information about the input images, and then using the [nueral-storyteller]("https://github.com/ryankiros/neural-storyteller") to generate longer form critiques based on pre-written examples. 

Auto Critique - In Progress Review 

###Information Gathering:

In order to produce generative art critiques, we need a database containing a considerable amount of previously human developed critiques. Finding critiques written in proper style is a fairly difficult task, considering most readily available information written about contemporary art is in the form of review, rather than direct critique. Consider the differences in structure between 

>The show, titled “unearthing treez,” was an extension of a body of work on view in a larger survey at the Museum of Arts and Design in New York through Apr. 3, 2016. That solo show and another scheduled to open in March at the Studio Museum of Harlem are the latest evidence of Patterson’s lightning rise in the art world since earning her master of fine arts degree in 2006.<sup>1</sup>

and

>The painting shows a contrast of light and dark colors.  The artist creates space by having the beach and people go back in the painting.  There are no real lines in the painting because it is painted in a pointilist style.<sup>2</sup>

Sifting through large amounts of information is necessary to train an effective model for the nueral-storyteller program which is integral to devleoping the final stage of the critiques. 

As it currently stands, I've compiled nearly 2,000 art critiques and reviews from [Art in America](http://www.artinamericamagazine.com/reviews/). The information has been separted into administrative portions, including artist name, reviewer name, date of article, etc. and the content of the review/critique itself.

### Utility Programs

In order to scrape all of this information I created a [python script](https://github.com/Luxapodular/AutoCritique/blob/master/Utilities/Scraping.py) which can quickly crawl the Art in America database, save and separate the information it finds. 

The python utility utilizes [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/#Download), a python based scraping utility library, and the [python simple requests library](http://docs.python-requests.org/en/latest/). This required quite a deep dive into the documention for these python libraries. 

### Next Steps 

The project is off to a good start. In the coming months I'll need to develop an automatic system to clean up the critiques, reviews and data that I've acquired. This will most likely require some natural language and regular expression parsing. 

I'll also need to begin ironing out a platform for these critiques to be served on. One suggestion was to create a Twitter bot which receives images and gives back critiques, which seems like a good first step. I'm not sure how stable the Twitter bot method would be. 


##### References 
<sup>1</sup>[Art in America Review](http://www.artinamericamagazine.com/reviews/ebony-g-patterson/)

<sup>2</sup>[Nicholas Orem](https://sites.google.com/a/pgcps.org/nicholas-orem-art/Home/homework-2-3/art-critique-example)
