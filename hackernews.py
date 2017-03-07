#!/usr/bin/env python3

# Web scraping utilities
from bs4 import BeautifulSoup
# Defacto http utilites
import requests
# Command line interface kit
import click

URL = 'https://news.ycombinator.com/'

# Function decorators for click
@click.command()
@click.option('--posts', default=1, help='Number of news articles to scrape.')
def hackernews(posts):
    """Simple command line application that scrapes Hacker News articles for a number of POSTS times."""
    articles = list()                           # Post meta-data list
    r = requests.get(URL)                       # Making the http request
    c = r.content                               # Getting the body
    soup = BeautifulSoup(c, 'html.parser')      # Parsing the content
    table = soup.find('table', 'itemlist')      # Anchoring to the itemlist table
    rows = table.find_all('tr')                 # Collecting all rows
    # List comprehension to merge the 2 data rows for each post
    items = [soupify(row, rows[i+1]) for i, row in enumerate(rows) if row.get('class') == ['athing']] 
    for item in items:
        # Try / except necessary to catch advertisment articles that don't allow for comments / author / scoring
        try:
            author      = item.find('td', 'subtext')('a')[0].get_text(),
            points      = item.find('td', 'subtext')('span')[0].get_text(),
            comments    = item.find('td', 'subtext')('a')[3].get_text()
            rank        = item.select('.rank')[0].get_text()[:-1] g 
        except IndexError:
            author      = 'null'
            points      = 'null'
            comments    = 'null'
            rank        = 'null'
        
        article = {
            'title':    item.select('.storylink')[0].get_text(),
            'uri':      item.select('.storylink')[0].get('href'),
            'author':   author,
            'points':   points,
            'comments': comments,
            'rank':     rank
        }
        articles.append(article)
    
    for x in articles:
        print(str(x))

def soupify(x, y):
    return BeautifulSoup((str(x) + str(y)), 'html.parser')

if __name__ == '__main__':
    hackernews()