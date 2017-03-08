# Hacker News Scraper
Simple command line application to scrape a user specified number of Hacker News articles and output as valid JSON

## How to run

The program can be run from any python 3.x compliant environment with access to pip for python for installing module dependancies, meaning you have a couple of options for setting up an enviroment.

* ### Basic Python install

 ***Windows***

Install Python 3.x on your machine, following the platform specific guidelines on the Python homepage under the downloads section.

> Ensure that during the installation you check the option to "install pip" and also "add python to path variable".

In a terminal, ensure you have the correct version of python with: `python -V` the ouput should be a version number in semvar format with 3.x.x

Clone the repo to a folder of your chosing and install the module dependancis via pip with the follwing: 

`pip install -r requirements.txt`

If all goes well you've downloaded the modules globally and can now proceed to run the program with the following: 

`python src/hackernews.py --posts n` 

where `n` is a value of your chosing to specific the number posts to download.

* ### Build Docker container (dockerfile) 

 ***Linux***

Have a working version of docker running on your linux distro.

Clone the repo to a directory of your chosing and cd into that repo.
Build the docker image from the dockerfile in the root of the repo using the following command in the terminal: 

`docker build -t <inset image name> .`

From here, simply run the newly created image using the following:

`docker run -it <name of image>`

This will spin up the container and place you in a shell inside the hacker-news-scraper repo. You can now proceed to run the program with the following: 

`python src/hackernews.py --posts n` 

where `n` is a value of your chosing to specific the number posts to download.


## Libraries used
A description of 3rd party modules used and why.

* #### [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/) - [Github](https://github.com/getanewsletter/BeautifulSoup4)
Beautiful Soup is a Python library for pulling data out of HTML and XML files. It's sole concern is providing idiomatic ways of navigating the parse tree of scraped documents. Since this task didn't require a spider / crawler, I felt a larger scraping framework such as Scrapy would have been overkill, when I can instead manually control the paging (which has the contraints of staying within the hacker news domain). The library provides all the necessary functionality and ease of use to pull the required data from the source, I'm also quite familiar with the library, having used it for a number of web scraping side projects in the past. It's relitively documented and well recommended with the python community.

* #### [Requests](http://docs.python-requests.org/en/master/) - [Github](https://github.com/kennethreitz/requests/)
Requests is a http library with a api that is a pleasure to work with. Most regard it as the defacto http library for python because of it's simplicity, security and functionality. It also has the most active community developing it in comparision to it's competitors, including the standard libs. I use this lib for any work regarding the web with python, since i'm familiar with the api, it is very documented and provided all the functionality I require, all with an elogant api :D

* #### [Click](http://click.pocoo.org/5/) - [Github](https://github.com/pallets/click)
From the homepage - "Click is a Python package for creating beautiful command line interfaces in a composable way with as little code as necessary. It’s the “Command Line Interface Creation Kit”. It’s highly configurable but comes with sensible defaults out of the box." It's a new library that I picked up for this task, since it came with so many out of the box goodies and making easy to understand, good-looking user interfaces for command line programs is an art of own without a capable library to help. After reading some reviews and looking at some example of popular command line creation libraries, I decided to pick the one that came well recommended, with the clearest api.
