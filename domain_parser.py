# Import libraries
import urllib
from bs4 import BeautifulSoup
from furl import furl

# define some variables
url_page = 'http://www.expireddomains.net/backorder-expired-domains/'
f = furl(url_page)
query_counter = 0
domain_size = 100
expired_domains = []

# Iterate through the tbody table, looking for the "field_domain" value
# to grab the 'title' aka expired domain


def expired_domain_parser(fu):
    # Query the site and return the sites html
    page = urllib.urlopen(fu.url)
    # Save the html as a beautiful soup object
    soup = BeautifulSoup(page, 'html.parser')
    # Parse the html and grab the tbody section
    body = soup.find('tbody')
    for ex in body.findAll('tr'):
        for expire in ex.find('td', {'class': 'field_domain'}):
            # When I remove this line it breaks so for now it stays
            for domain in expire:
                dom = expire.find('title')
            for e in body.findAll('li'):
                e.extract()
        expired_domains.append(domain)

# Affixes the proper 'query' parameter to the url


def url_append(qc, ds):
    if not expired_domains:
        while True:
            f.add(args={'start': [qc]})
            # prints out the urls we want to query so we can check they're correct
            expired_domain_parser(f)
            #print(f.url)
            del f.args['start']
            qc = qc + 25
            # cuts off loop at "domain_size"...
            # got by dividing total number of domains by 25 (# results displayed on page)
            # to improve, need to parse and grab total number of domains, divide by 25, and
            # set a "breaker" variable to that value that will be used to cut off the loop
            if qc > ds:
                break


url_append(query_counter, domain_size)
print(', '.join(expired_domains))

