# Import libraries
import urllib
from bs4 import BeautifulSoup
from furl import furl

# define some variables
url_page = 'http://www.expireddomains.net/backorder-expired-domains/'
f = furl(url_page)
query_counter = 0
domain_size = 1000
expired_domains = []

# Query the site and return the sites html
page = urllib.urlopen(f.url)

# Save the html as a beautiful soup object
soup = BeautifulSoup(page, 'html.parser')

# Parse the html and grab the tbody section
body = soup.find('tbody')


# Iterate through the tbody table, looking for the "field_domain" value
# to grab the 'title' aka expired domain

def expired_domain_parser(pg):
    for ex in pg.findAll('tr'):
        for expire in ex.find('td', {'class': 'field_domain'}):
            for domain in expire:
                dom = expire.find('title')
            for e in pg.findAll('li'):
                e.extract()
        expired_domains.append(domain)


# Affixes the proper 'query' parameter to the url

def url_append(qc, ds):
    if not expired_domains:
        while True:
            f.add(args={'start': [qc]})
            # prints out the urls we want to query so we can check they're correct
            print(f.url)
            del f.args['start']
            qc = qc + 25
            # cuts off loop at 8500... got by dividing total number of domains by 25 (# results displayed on page)
            # to improve, need to parse and grab total number of domains, divide by 25, and
            # set a "breaker" variable to that value that will be used to cut off the loop
            if qc > ds:
                # print the scraped domains
                print(', '.join(expired_domains))
                break


# function tests
# url_append(query_counter, domain_size)
# expired_domain_parser(body)
# print(', '.join(expired_domains))
