#!/usr/bin/env python3

# Maintaining ordered output
from collections import OrderedDict
# URI schema checking
from urllib.parse import urlparse
# Web scraping utilities
from bs4 import BeautifulSoup
# JSON conversion
from json import dumps
# Defacto http utilites
import requests
# Command line interface kit
import click

BASEURL = 'https://news.ycombinator.com/news?p='

# Function decorators for click
@click.command()
@click.option('--posts', required=True, type=click.IntRange(1, 100), help='Number of news articles to scrape.')
def hackernews(posts):
    """Simple command line application to scrape a user specified number of Hacker News articles."""

    pages = int(posts / 30) + 1                 # Calculating the number of pages to scrape
    result = list()                             # Result list
    
    for page in range(1, pages + 1):
        url = BASEURL + str(page)                   # Construct page specific url
        r = requests.get(url)                       # Making the http request
        c = r.content                               # Getting the body
        bs4 = BeautifulSoup(c, 'html.parser')       # Parsing the content
        result += scrape(page, posts, bs4)

    # Converting the list of dicts to JSON and printig to STDOUT
    print(dumps(result, indent=4, separators=(',', ': ')))


# Responsible for performing scraping and error handling
def scrape(page, posts, bs4):

    table = bs4.find('table', 'itemlist')      # Anchoring to the itemlist table
    rows = table.find_all('tr')                 # Collecting all rows

    # List comprehension to merge 2 data rows for each article
    items = [merge(row, rows[i+1]) for i, row in enumerate(rows) if row.get('class') == ['athing']]

    # Slice the resulting list if on the last page
    if int(posts / 30) + 1 == page:
        items = items[:(posts % 30)]

    articles = list()
    # For each article scrape the following values
    for item in items:
        title 	= item.select('.storylink')[0].get_text()
        uri 	= item.select('.storylink')[0].get('href')
        rank    = item.select('.rank')[0].get_text()[:-1]
        # Try / except necessary to catch advertisment articles that don't show comments / author / scoring
        try:
            author  = item.find('td', 'subtext')('a')[0].get_text()
            points  = item.find('td', 'subtext')('span')[0].get_text()
            comments = item.find('td', 'subtext')('a')[3].get_text()
        except IndexError:
            author = 'empty'
            points = '0'
            comments = '0'
        
        # Handling the difference comment lengths
        if comments == 'discuss': comments = '0'
        elif "comments" not in comments: comments = comments[:-len('\u00a0comment')]
        else: comments = comments[:-len('\u00a0comments')]
        
        # Handling the case of point singular or plural
        if "points" not in points: points = points[:-len(' point')]
        else: points = points[:-len(' points')]

        # Handling for empty
        if not title: title = 'empty'
        if not author: author = 'empty'
        
        # Handling for over 256 characters
        if len(title) > 256: title = title[:256]
        if len(author) > 256: author = author[:256]
        
        # Handling integers less that zero
        if not points: points = '0'
        elif int(points) < 0: points = '0'
        if not comments: comments = '0'
        elif int(comments) < 0: comments = '0'
        if not rank: rank = '0'
        elif int(rank) < 0: rank = '0'
        
        # Handling for invalid URI
        o = urlparse(uri)
        if not o.scheme or not o.netloc:
            uri = 'invalid'

        # Creating a dict per article
        article = OrderedDict([
            ('title', title),
            ('uri', uri),
            ('author', author),
            ('points', points),
            ('comments', comments),
            ('rank', rank)
        ])
        articles.append(article)

    # Return the list of articles
    return articles

# Helper function to convert & merge input as strings, returning bs4 object
def merge(left, right):
    return BeautifulSoup((str(left) + str(right)), 'html.parser')

if __name__ == '__main__':
    hackernews()