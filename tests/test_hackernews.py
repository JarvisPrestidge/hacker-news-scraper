# Import my module
from hackernews.hackernews import scrape, merge
# Need BeautifulSoup for parsing static html
from bs4 import BeautifulSoup

# Setup
with open("test.html", encoding="utf-8") as f:
    html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    # Passing in 1 page (i.e. test.html) & 2 posts 
    articles = scrape(1, 2, soup)

def test_strings_over_256_characters():
    assert len(articles[0]['title']) <= 256
    assert len(articles[0]['author']) <= 256
    
def test_empty_strings():
    assert articles[1]['title'] != ''
    assert articles[1]['title'] == 'empty'
    assert articles[1]['author'] != ''
    assert articles[1]['author'] == 'empty'

def test_correct_uri_parsing():
    assert articles[0]['uri'] == 'invalid'
    assert articles[1]['uri'] != 'invalid'
    assert articles[1]['uri'] == 'https://tomassetti.me/antlr-mega-tutorial'

def test_greater_than_zero_values():
    assert int(articles[0]['points']) >= 0
    assert int(articles[0]['comments']) >= 0
    # Must be greater than 0, can't be 0
    assert int(articles[0]['rank']) > 0
    
def test_is_integer_value():
    try:
        int(articles[0]['points'])
        int(articles[0]['comments'])
        int(articles[0]['rank'])
        assert True
    except ValueError:
        assert False