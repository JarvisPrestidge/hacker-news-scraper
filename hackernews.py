#!/usr/bin/env python3

# Maintaining ordered output
from collections import OrderedDict
# Web scraping utilities
from bs4 import BeautifulSoup
# Defacto http utilites
import requests
# Command line interface kit
import click
# JSON conversion
import json

base_url = 'https://news.ycombinator.com/'

# Function decorators for click
@click.command()
@click.option('--posts', required=True, type=click.IntRange(0, 100), help='Number of news articles to scrape.')
def hackernews(posts):
    """Simple command line application that scrapes Hacker News articles for a number of POSTS times."""
    
    pages = int(posts / 30) + 1                 # Calculating the numbe of pages to scrape
    result = list()                             # Result list
    for page in range(pages):
        result += scrape(page + 1, posts)       # Page needs to be incremented by 1 since range start from 0
        print(result)
    print(json.dumps(result, sort_keys=False))
    

def scrape(page, posts):
    
    url = base_url + '/news?p=' + str(page)     # Construct page specific url
    r = requests.get(url)                       # Making the http request
    c = r.content                               # Getting the body
    soup = BeautifulSoup(c, 'html.parser')      # Parsing the content
    table = soup.find('table', 'itemlist')      # Anchoring to the itemlist table
    rows = table.find_all('tr')                 # Collecting all rows
    
    # List comprehension to merge the 2 data rows for each article, then slice the resulting list by the posts arg
    items = [merge(row, rows[i+1]) for i, row in enumerate(rows) if row.get('class') == ['athing']][:posts] 
    
    articles = list()                           # List to hold individual articles
    for item in items:
        title 	= item.select('.storylink')[0].get_text()
        uri 	= item.select('.storylink')[0].get('href')
        author  = item.find('td', 'subtext')('a')[0].get_text()
        points  = item.find('td', 'subtext')('span')[0].get_text()
        rank    = item.select('.rank')[0].get_text()[:-1] 
        
        # Try / except necessary to catch advertisment articles that don't allow for comments / author / scoring
        try:
            comments = item.find('td', 'subtext')('a')[3].get_text()[:-len('\u00a0comments')]
            comments if comments != 'discuss' else str(0)
        except IndexError:
            # Setting to null if not found
            author = 'null'
            points = 'null'
            comments = 'null'
            
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
    # Return the list of articlesk
    return articles

# Hleper function to convert & merge input as strings, returning bs4 object
def merge(left, right):
    return BeautifulSoup((str(left) + str(right)), 'html.parser')

if __name__ == '__main__':
    hackernews()